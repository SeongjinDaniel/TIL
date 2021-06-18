# 20200511 R Crawling

 css 선택자를 잘 활용해서 개발했어야 했는데 그러지 못함.

select 태그에서 많은 option에서 selected된 선택자의 value를 가져왔어야하는데 헤맸음.

```R
selectYear <- remDr$findElement(using='css',"#inspectYear > option[selected]")
              selectYear$getElementText()
```

# 개발 소스

```R
# 참가격 사이트 생필품가격정보 크롤링

install.packages("RSelenium")
library(RSelenium)

remDr <- remoteDriver(remoteServerAddr = "localhost" , port = 4445, browserName = "chrome")
remDr$open()
url<-'https://www.price.go.kr/tprice/portal/dailynecessitypriceinfo/priceiteminfo/getPriceItemInfoList.do'
remDr$navigate(url)
Sys.sleep(5)

# 대형마트, 백화점, .. 등 모든 유형 체크!!
#chk_LM #대형마트
clickStore <- function(){
  clickCheck <- remDr$findElement(using='css',"#chk_LM")
  clickCheck$clickElement()
  #chk_DP # 백화점
  clickCheck <- remDr$findElement(using='css',"#chk_DP")
  clickCheck$clickElement()
  #chk_SM # 슈퍼마켓
  clickCheck <- remDr$findElement(using='css',"#chk_SM")
  clickCheck$clickElement()
  #chk_TR # 전통시장
  clickCheck <- remDr$findElement(using='css',"#chk_TR")
  clickCheck$clickElement()
  #chk_CS # 편의점
  clickCheck <- remDr$findElement(using='css',"#chk_CS")
  clickCheck$clickElement()
  Sys.sleep(1)
}
clickStore()


# 분기, 지역, 품목, 상품마다 클릭해서 크롤링
# 분기 //*[@id="inspectDay"]
# 지역 //*[@id="entpAreaCode"]
# 품목 //*[@id="goodSmlclsCode"]
# 상품 //*[@id="goodId"]
clickType <- function(optionType, index){
  selectInfo <- paste("//*[@id=\"",optionType,"\"]/option[",index,"]", sep="")
  try(optionDay <- remDr$findElement(using='xpath', value=selectInfo), silent=T)
  return(optionDay)
}

# # 지역마다 클릭해서 크롤링
# clickLocation <- function(index){
#   selectInfo <- paste("//*[@id=\"entpAreaCode\"]/option[",index,"]", sep="")
#   try(optionLoc <- remDr$findElement(using='xpath', value=selectInfo), silent=T)
#   return(optionLoc)
# }
# 
# # 품목마다 클릭해서 크롤링
# clickProductType <- function(index){
#   selectInfo <- paste("//*[@id=\"goodSmlclsCode\"]/option[",index,"]", sep="")
#   try(optionPro <- remDr$findElement(using='xpath', value=selectInfo), silent=T)
#   return(optionPro)
# }
# 
# #상품마다 클릭해서 크롤링
# clickProduct <- function(index){
#   selectInfo <- paste("//*[@id=\"goodId\"]/option[",index,"]", sep="")
#   try(optionPro <- remDr$findElement(using='xpath', value=selectInfo), silent=T)
#   return(optionPro)
# }

repeat{
  optionDay <- NULL
#--------------------------------------------------------------------------------------
  # 1~4분기 실행
  for(indexQuarter in 1:4){
    # day 클릭
    optionDay <- NULL
    optionLoc <- NULL
    optionProType <- NULL
    optionPro <- NULL
    indexLoc <- 1
    indexProType <- 1
    indexPro <- 1
    #print(quarterIndex)
    
    optionDay <- clickType("inspectDay", indexQuarter)
    
    if(is.null(optionDay)) {
      cat("종료\n")
      break;
    }
    # 지역 클릭
    repeat{
      optionLoc <- NULL
      optionLoc <- clickType("entpAreaCode", indexLoc)
      indexLoc <- indexLoc + 1
      if(is.null(optionLoc)) {
        cat("종료\n")
        break;
      }
      optionLoc$clickElement()
      Sys.sleep(1)
      
      # 판매점 전체로만 클릭해서 사용!! -> 따로 클릭 안해도됨 default가 전체임
      # 품목 클릭
      repeat{
        optionProType <- NULL
        optionProType <- clickType("goodSmlclsCode", indexProType)
        indexProType <- indexProType + 1
        if(is.null(optionProType)) {
          cat("종료\n")
          break;
        }
        optionProType$clickElement()
        Sys.sleep(1)
        
        # 상품 클릭 (전체로하면 안됨)
        repeat{
          optionPro <- NULL
          optionPro <- clickType("goodId", indexPro)
          indexPro <- indexPro + 1
          if(is.null(optionPro)) {
            cat("종료\n")
            break;
          }
          optionPro$clickElement()
          Sys.sleep(1)
          # 조회 클릭
          clickFind <- remDr$findElement(using='css',"#search_btn")
          clickFind$clickElement()
          Sys.sleep(1)
          
          # 밑에 탭에 대형마트, 백화점, 슈퍼마켓, 전통시장, 편의점 순으로!! 크롤링
          # #tab_menu > ul > li.on > span > a           ---전체
          # #tab_menu > ul > li:nth-child(2) > span > a --- 대형마트
          # #tab_menu > ul > li:nth-child(3) > span > a --- 백화점
          # #tab_menu > ul > li:nth-child(4) > span > a --- 슈퍼마켓
          # :
          # #tab_menu > ul > li:nth-child(6) > span > a --- 편의점
          for(index in 2:6){
            # 여기서 부터 상품 크롤링 !!ㅎㅎㅎ ...
            # 
            selectInfo <- paste("#tab_menu > ul > li:nth-child(",index,") > span > a", sep="")
            click_Stores <- remDr$findElement(using='css', selectInfo)
            click_Stores$clickElement()
            Sys.sleep(1)
            
            # 전체 물품들 크롤링 해서 가져오기
            # 전체 상품 개수 확인
            #tab_menu > ul > li:nth-child(2) > span > a
            #tab_menu > ul > li:nth-child(3) > span > a
            #tab_menu > ul > li:nth-child(4) > span > a
            sizeCss <- paste("#tab_menu > ul > li:nth-child(",index,"4) > span > a", sep="")
            size <- remDr$findElement(using='css', sizeCss)
            storeType <- size$getElementText()
            limit <- gsub("[^[:digit:]]", "", storeType)
            limit
            
            ## 여기부터!!!!!!!!!!!!!!!!!!!!!!
            if(limit <= 10){
              selectYear <- remDr$findElement(using='css',"#inspectYear > option[selected]")
              selectYear$getElementText()
              try(year <- remDr$findElement(using='css', value=selectYear), silent=T)
              year$getElementText()
            }else{
              
            }
            

            selectInfo <- paste("#mCSB_3_container > ul > li:nth-child(",index,")", sep="")
            info <- remDr$findElement(using='css',selectInfo)
            # infoTag <- info$getElementTagName()
            infoTxt <- info$getElementText()
            
            
            url <- "https://comic.naver.com/genre/bestChallenge.nhn"
            text <- read_html(url)
            temp <- html_nodes(text, sizeCss)
            txtName <- html_text(temp, trim=TRUE)
            # #schForm > table > tbody > tr > td
            # #resultTable > tbody > tr:nth-child(1) > td:nth-child(1)
            # #resultTable > tbody > tr:nth-child(1) > td:nth-child(2)
            # #resultTable > tbody > tr:nth-child(2){행} > td:nth-child(2){열}
            
            size <- remDr$findElements(using='css selector', sizeCss)
            limit <- sapply(size, function(x){x$getElementText()})
            

          }
        }

      }
      
    }

    optionDay$clickElement()
  }
  if(is.null(optionDay)) {
    cat("종료\n")
    break;
  }
  
}


# Test# Test# Test# Test# Test# Test# Test# Test# Test# Test# Test# Test
clickCheck <- remDr$findElement(using='css',"#search_btn")
clickCheck$clickElement()


# resultTable > tbody > tr:nth-child(1) > td:nth-child(1)
clickCheck <- remDr$findElement(using='css',"# resultTable > tbody > tr:nth-child(1) > td:nth-child(1)")
clickCheck$clickElement()

selectInfo <- paste("//*[@id=\"inspectYear\"]", sep="")
try(tt <- remDr$findElement(using='xpath', value=selectInfo), silent=T)
tt$getElementText()

#inspectYear > option.selected
#inspectYear > option:nth-child(2)
aa <- remDr$findElement(using='css',"#inspectYear > option[selected]")
aa$getElementText()
clickCheck$clickElement()
```

