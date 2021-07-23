# Ajax 사용 예제



```javascript
$.ajax({
    type: "POST",
    enctype: "multipart/form-data",
    url: "/drawing-boards",
    data: formData,
    processData: false,
    contentType: false,
    statusCode: {
        401: function (data) {
            console.log(data);
        }
    },
    // async: false,
    success: function (data, status) {
        console.log(status);
        console.log(data.status);
        console.log("===============");
        if (data['success']) {
            alert("파일업로드 성공");
        }

    },
    error: function (request, status, error) {
        console.log(request.responseText);
        let val = request.responseText.split(/[\r\n|\r|\n|{|}|:|,|\[|\]]/gi);
        console.log(val[val.length - 2]);
        console.log(request.status);
        if (request.status === 401) {
            alert("로그인 후 글쓰기가 가능합니다. 먼저 로그인을 하시기 바랍니다.");
        } else if (request.status === 400) {
            alert("제목 또는 내용의 공백으로 게시글을 등록할 수 없습니다.");
        } else {
            alert("파일 확장자를 지원하지 않습니다. 해당하는 사진을 제거하고 다시 시도해주시기 바랍니다.");
        }
        return false;
    }
});
```