# S3 File upload source code



```java
@Service
public class S3FileUploadService implements FileUploadService {

    private final ZonedDateTime zonedDateTime;
    private final Environment env;
    private AmazonS3 s3Client;

    public S3FileUploadService(Environment env) {
        this.zonedDateTime = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
        this.env = env;
    }

    /**
     * s3 정보 초기화 의존성 주입이 이루어진 후 초기화를 수행, bean이 한 번만 초기화.
     */
    @PostConstruct
    private void initializeS3Client() {
        AWSCredentials credentials = new BasicAWSCredentials(
                Objects.requireNonNull(env.getProperty(AmazonS3Keys.accessKey), "aws accessKey"),
                Objects.requireNonNull(env.getProperty(AmazonS3Keys.secretKey), "aws secretKey"));

        s3Client = AmazonS3ClientBuilder.standard()
                .withCredentials(new AWSStaticCredentialsProvider(credentials))
                .withRegion(env.getProperty(AmazonS3Keys.region))
                .build();
    }

    /**
     * s3에 파일 업로드.
     * 파일 업로드시 지정된 파일을 저장하려는 aws s3 path를 지정해서 저장한다.
     *
     * @param uploadFile 업로드 파일.
     * @return s3 url 문자열 반환.
     * @throws IOException uploadFile.getInputStream()에서 파일 예외 처리.
     */
    @Override
    public String upload(MultipartFile uploadFile, String filePath) {
        String fileName = "";
        String md5Checksum = SecurityService.getMD5Checksum(uploadFile.getOriginalFilename());
        String baseFileName =
                zonedDateTime.format(DateTimeFormatter.ofPattern("yyyy_MM_dd")) +
                        "/" +
                        zonedDateTime.format(DateTimeFormatter.ofPattern("yyyyMMdd")) +
                        "_" +
                        md5Checksum +
                        "/" +
                        SecurityService.getZeroToNineByRandom() +
                        "_" +
                        System.currentTimeMillis();
        String fileFullName = Objects.requireNonNull(uploadFile.getOriginalFilename(), "file fail");
        String extension = fileFullName.substring(fileFullName.lastIndexOf(".") + 1);
        if (filePath.isBlank()) {
            throw new IllegalStateException("upload, " + fileFullName);
        }
        String bucket = env.getProperty(AmazonS3Keys.bucket);
        ObjectMetadata metadata = new ObjectMetadata();
        metadata.setContentType(uploadFile.getContentType());
        try {
            fileName = filePath + baseFileName + "." + extension;
            s3Client.putObject(new PutObjectRequest(
                bucket,
                fileName,
                uploadFile.getInputStream(),
                metadata));
        } catch (IOException e) {
            throw new IllegalStateException("서버에서 파일 처리중 예상치 못한 에러가 발생했습니다");
        }
        return s3Client.getUrl(bucket, fileName).toString();
    }
}
```

