# jsp javascript에서 Ajax를 이용하여 Controller와 응답하기

이 질문에 대한 답변을 정확하게 이해하기 위해서는, 웹 요청과(Request) 응답(Response), Servlet과 JSP에 대한 지식이 필요하며,

아울러 Java.io 패키지와 연관이 있는 Stream이라는 것에 대해서도 알아야할 필요가 있습니다.

대충 질문하신 분의 코드를 보아하니, Servlet의 doGet 혹은 doPost 메서드 내부에서 나올 법한 코드인 것 같습니다.



response 변수에 대해 설명을 드리자면, Servlet의 doGet 혹은 doPost 함수의 파라미터로 아마 response 변수를 만들어 놓았을 것입니다. 이 response 변수에 실제 객체를 할당해주는 것은 Servlet Container(공부할 때는 주로 Tomcat을 많이 쓰죠)가 알아수 해주기 때문에 개발자는 신경을 전혀(?) 쓸 필요가 없습니다.

보통 어떠한 Servlet으로 요청이 들어오게 되면, 그 요청을 파악을 해서 어떠한 응답을 클라이언트로 보내야하는지에 대한 분석이 이루어집니다.

흔히 클라이언트로부터 Servlet으로 요청이 들어오게 되면, 요청 파라미터라는 것이 같이 오게 되는데,

이것에 대한 분석은 request.getParameter("someKey") 이러한 식으로 파악을하게 되죠.

요청을 파악했다면, 클라이언트로 내보낼 응답을 작성해야 합니다.

대부분의 웹 프로그래밍은 응답을 텍스트로 작성하며, 이 텍스트는 HTML 페이지의 모양을 하고 있게됩니다.

물론 모두 그렇지는 않습니다.

여튼 응답으로 텍스트를 기록해야하는데,

이 때 스트림이라는 개념이 나옵니다. 말 그대로 데이터의 흐름이라고 보시면됩니다.

Servlet에서는 클라이언트 쪽으로 보내는 데이터의 흐름을 건드려야할 필요가 있습니다.

위에서 언급했던 response 변수를 활용하면 응답과 관련된 많은 작업들을 수행할 수 있습니다.

응답 스트림에 텍스트를 기록하는 것도 가능하며, 이 작업을 하기 위해서 response.getWriter();를

호출해야 합니다.

보통 스트림에는 바이너리 기반의 스트림과, 텍스트 기반의 스트림이 있습니다.

보통 바이너리 기반의 스트림은 InputStream(입력), OutputStream(출력)이라는 것으로 끝나고,

텍스트 기반의 스트림은 Reader(입력), Writer(출력)로 끝납니다.

언급했듯이 Servlet으로 들어온 요청은 대체로 텍스트(HTML)로 응답을 보내기 때문에,

PrintWriter out = response.getWriter(); 이런 식으로 응답으로 내보낼 출력 스트림을 얻어낸 후,

out.println("<html><body>Hello World!</body></html>"); 이런 식으로 스트림에 텍스트를 기록하게 됩니다.

보시다시피 이러한 웹 프로그래밍 방식은 굉장히 빡세기 때문에 이걸 해결하기 위해 훗날 JSP가 등장하였고,

그 JSP도 빡세다는 시대의 흐름에 의해 요새는 다른 방식으로 개발 방법이 진화하고 있는 것이,

현재 Java Web Programming의 추세입니다.**[출처]** [PrintWriter out = response.getWriter(); ](http://blog.naver.com/min_sub/80069919296)|**작성자** [에르메스](http://blog.naver.com/min_sub)

--------

 자바에서 웹으로 데이터를 출력하기 위해 PrintWriter를 사용한다. 

서블릿 생명주기에 따라 생성된 요청객체와 응답객체는 doGet 메서드를 통해 html 콘텐츠를 생성하는데 이때 원하는 내용을 출력하기 위한 코드이다. 

**PrintWriter out= response.getWriter();**

 PrintWriter는 new로 초기화 하지 않고 바로 사용할 수 있다. 

```java
public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException{
    response.setContentType("text/html");
    response.setCharacterEncoding("utf-8");
    // PrintWriter java에서 웹으로 출력 시
    PrintWriter out= response.getWriter();
    out.print("Servlet works<br>");


출처: https://improver.tistory.com/196 [문돌이의IT]
```

---------------

#### Controller

```java
   @RequestMapping(value = "/cart", method = RequestMethod.POST)
   @ResponseBody
   // insert update
   public void cartPost(Model model,String action, GoodsEventShopMemberVO vo, HttpServletResponse response) throws ServletException, IOException{      

      if (action.equals("insert")) {
         mh.insertCart(vo,response);
         
      }else if (action.equals("delete")) {
         mh.deleteCart(response);   
      }

   }
```

#### JSP

```java
//클릭 상품 저장
      function add(good_id){
         $.ajax({
            type :"post",
            url :"/pmkim/cart",  
            data : {"action" : "insert",
                  "good_id" : good_id},
            dataType : "json",   // text, xml, html, script, json, jsonp 가능 
            success : function(data){   
               if(data=="1"){

                  var key = [];         //id값 담을 변수 선언
                  var num = document.getElementsByClassName('good_id').length
                  for(var i=0; i<num; i++){
                     key[i] = document.getElementsByClassName('good_id')[i].value;
                  }
                  var good_name = document.getElementsByClassName('good_name')[key.indexOf(good_id)].innerHTML;
                  var good_img = document.getElementsByClassName('img-fluid')[key.indexOf(good_id)].getAttribute('src');

                  document.getElementById('cart-View').innerHTML = "<p id='result_name'>"+ good_name + "</p> <br>"+"<img src = '"+good_img+"' class ='img-fluid'>";

               }else{
                  alert("상품이 선택되지 않았습니다.");
               }
            },
            error : function(){
               alert("프로그램 에러가 발생했습니다.");
            }
         });
         
      }
```

#### Service

```java
public void insertCart(GoodsEventShopMemberVO vo, HttpServletResponse response) throws IOException{
      if(cdao.cartInsert2(vo)) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }
```

# Service 전체

```java
package service;

import java.io.IOException;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import dao.CartDAO;
import vo.GoodsEventShopMemberVO;
import vo.GoodsInformVO;

@Repository
@Service
public class ManHappyService {
   
   @Autowired
   CartDAO cdao;
   
   //카테고리 체크해줌
   public void checkCtg(String good_id,HttpServletResponse response) throws IOException{
      if(cdao.checkCtg(good_id)!=null) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }
   
   public void insertCart(GoodsEventShopMemberVO vo, HttpServletResponse response) throws IOException{
      if(cdao.cartInsert2(vo)) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }

   public void deleteCart(HttpServletResponse response) throws IOException{
      if(cdao.cartDelete2()) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }
   
   public List<GoodsEventShopMemberVO> getNameImg(String good_id) {
      return cdao.getNameImg(good_id);
   }
   
   public void recomGoods(String ctg_3,int min, int max, HttpServletResponse response) throws IOException{
      List<GoodsInformVO> list = cdao.recomGoodsList(ctg_3, min, max);
      if(list != null) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }
   
   public void test(String ctg_3, HttpServletResponse response) throws IOException{
      List<GoodsInformVO> list = cdao.test(ctg_3);
      if(list != null) {
         response.getWriter().print("1");
      }else {
         response.getWriter().print("0");
      }
   }
}
```

# Controller 전체

```java
package spring.mvc.pmkim;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import dao.CartDAO;
import service.ManHappyService;
import service.PagingService;
import vo.GoodsEventShopMemberVO;
import vo.GoodsInformVO;

@Controller
public class CartController {

   @Autowired
   CartDAO cdao;
   
   @Autowired
   PagingService ps;
   
   @Autowired
   ManHappyService mh;
   
   @RequestMapping(value = "/cart", method = RequestMethod.GET)
   // delete search listone
   public ModelAndView cartGet(String action, String keyword, GoodsEventShopMemberVO gesmvo, String event_name,String shop_code, @RequestParam(defaultValue="1")int pgNum) {
      ModelAndView mav = new ModelAndView();
      //paging용 시작페이지 num, 끝페이지 num
      int startNum = ps.getWritingStart(pgNum);
      int endNum = ps.getWritingEnd(pgNum);
      
      int end = ps.getPageCount(keyword);
      int pageEnd = ps.getPageEnd(pgNum, keyword);
      boolean nextdata = ps.isNextData(pgNum, keyword);
      //쿼리저장
      String oldQ ="";
   
      //default값 설정
      if(event_name==null && shop_code==null) {
         event_name = "1+1";
         shop_code = "GS";
      }
      
      List<GoodsEventShopMemberVO> geslist = cdao.goodsShopEvent(event_name,shop_code,startNum,endNum);
      
      if (action != null && keyword != null) {                     //search
         geslist = cdao.searchGoodsPaging(keyword, startNum, endNum);
         oldQ += "&action="+action+"&keyword="+keyword;
         
      } else if (action != null && keyword ==null){                  //sort
         
         geslist = cdao.goodsShopEvent(event_name,shop_code,startNum,endNum);
         oldQ += "&action="+action+"&event_name="+event_name+"&shop_code="+shop_code;
         end = ps.getPageCount(event_name, shop_code);
         pageEnd = ps.getPageEnd(pgNum, event_name, shop_code);
         nextdata = ps.isNextData(pgNum, event_name, shop_code);
   
      }
      
      mav.addObject("pgNum",pgNum);
      mav.addObject("oldQ",oldQ);
      mav.addObject("end",end);
      mav.addObject("pageStart",ps.getPageStart(pgNum));
      mav.addObject("pageEnd",pageEnd);
      mav.addObject("preData",ps.isPreData(pgNum));
      mav.addObject("nextData",nextdata);
      mav.addObject("gesList", geslist);
      mav.setViewName("mycart");
      return mav;
   }

   @RequestMapping(value = "/cart", method = RequestMethod.POST)
   @ResponseBody
   // insert update
   public void cartPost(Model model,String action, GoodsEventShopMemberVO vo, HttpServletResponse response) throws ServletException, IOException{      

      if (action.equals("insert")) {
         mh.insertCart(vo,response);
         
      }else if (action.equals("delete")) {
         mh.deleteCart(response);   
      }

   }
   
   //만원의 행복
   @RequestMapping(value="/happy", method = RequestMethod.GET)
   @ResponseBody
   public void happyGet(Model model, String maxM, String minM, GoodsInformVO givo, HttpServletResponse response) throws ServletException, IOException{
      int max = Integer.parseInt(maxM.replace(",", ""));
      int min = Integer.parseInt(minM.replace(",",""));
      GoodsInformVO vo2 = cdao.checkCtg(givo.getGood_id());
      int num = cdao.countCtg3(vo2.getCtg_3());
      int rand = (int)(Math.random() * num);
      List<GoodsInformVO> gilist = cdao.test(vo2.getCtg_3());
      System.out.println("num : " + num + ",rand : "+ rand + ",gilist : "+ gilist.size());
      //int maxA[] = new int[num];
      //int minA[] = new int[num];
      if(gilist.get(rand).getGood_price().equals("NONE")) {
         System.out.println("none이면 제외");
      }else {
         max = max-Integer.parseInt(gilist.get(rand).getGood_price().replace(",", ""));
         min = min-Integer.parseInt(gilist.get(rand).getGood_price().replace(",", ""));
      }
      System.out.println(min + ", "+ max);
      
      /*
      for(int i=0; i<gilist.size(); i++) {
         if(gilist.get(i).getGood_price().equals("NONE")) {
            maxA[i] = max;
            minA[i] = min;
         }else {
            maxA[i] = max-Integer.parseInt(gilist.get(i).getGood_price().replace(",", ""));
            minA[i] = min-Integer.parseInt(gilist.get(i).getGood_price().replace(",", ""));
         }
         
         System.out.println(minA[i] + ", "+ maxA[i]);
      }
      */
      mh.test(vo2.getCtg_3(), response);
      
      //model 객체로 보내기
   }
   
}
```

# Mapper 전체

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
 PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
 "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
 
<mapper namespace="resource.CartMapper">
   <select id="selectCart" resultType="vo.GoodsEventShopMemberVO">
      select c.cart_id as cart_id,m.id as id,c.good_id as good_id, c.cnt as cnt, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img
      from cart c, member m, goods g
      where c.id = m.id
      and g.good_id = c.good_id
      and m.id = #{id}
   </select>
   
   <!-- 20.05.28 - delete, insert 1버전은 로그인 구현 후 사용 -->
   
   <delete id="deleteCart" parameterType="String">
      delete from cart where id=#{id}
   </delete>
   
   <!-- 2버전은 전체 cart 데이터 삭제 -->
   <delete id="deleteCart2">
      delete from cart
   </delete>

   <insert id="insertCart" parameterType="vo.CartVO">
      <selectKey resultType="_int" keyProperty="cart_id" order="BEFORE">
         select cart_seq.nextval from dual
      </selectKey>
      insert into cart (cart_id, id, good_id, cnt) values (#{cart_id},#{id},#{good_id},#{cnt})
   </insert>
   
   <!-- 2버전은 id,cnt null 값 -->
   <insert id="insertCart2" parameterType="vo.GoodsEventShopMemberVO">
      <selectKey resultType="_int" keyProperty="cart_id" order="BEFORE">
         select cart_seq.nextval from dual
      </selectKey>
      insert into cart (cart_id, good_id) values (#{cart_id},#{good_id})
   </insert>
   
   <select id="searchGoods" resultType="vo.GoodsEventShopMemberVO">
      select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img 
      from goods g, event e, shop_code sc, goods_shop gs
      where g.good_id = e.good_id
        and sc.shop_code=gs.shop_code
        and gs.good_id = g.good_id
        and g.good_name like '%'||#{keyword}||'%'
   </select>
   
   <select id="listCount" resultType="_int" parameterType="java.util.HashMap"> <!-- paging하기 위해 갯수 count -->
        select count(g.good_id) 
        from goods g, event e, shop_code sc, goods_shop gs 
        where g.good_id = e.good_id
        and sc.shop_code=gs.shop_code
        and gs.good_id = g.good_id
        and e.event_name = #{event_name}
        and sc.shop_code = #{shop_code}
     </select>
     
     <select id="goodsListAll" resultType="vo.GoodsEventShopMemberVO">
        select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img 
      from goods g, event e, shop_code sc, goods_shop gs
      where g.good_id = e.good_id
        and sc.shop_code = gs.shop_code
        and gs.good_id = g.good_id

     </select>
     
     <select id="goodsList_shopEvent" resultType="vo.GoodsEventShopMemberVO" parameterType="java.util.HashMap"> <!-- shop&eventname으로 검색 -->
        select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img , g.search_date as search_date 
      from goods g, event e, shop_code sc, goods_shop gs
      where g.good_id = e.good_id
        and sc.shop_code=gs.shop_code
        and gs.good_id = g.good_id
        and e.event_name = #{event_name}
        and sc.shop_code = #{shop_code}
     </select>
     
     <select id="goodsList_shopEvent_paging" resultType="vo.GoodsEventShopMemberVO" parameterType="java.util.HashMap"> <!-- shop&eventname으로 검색 -->
        select shop_name, event_name, good_id, good_name, good_price, good_img , search_date, shop_code 
      from (select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img , g.search_date as search_date, sc.shop_code as shop_code, rownum as rnum 
            from goods g, event e, shop_code sc, goods_shop gs
            where g.good_id = e.good_id
              and sc.shop_code = gs.shop_code
              and gs.good_id = g.good_id
              and e.event_name = #{event_name}
                and sc.shop_code = #{shop_code})
      where rnum between #{startNum} and #{endNum}
     </select>
     
     <!-- 20.05.26 추가 -->
     <select id="foodsCtg" resultType="vo.GoodsInformVO">
        select distinct ctg_1, ctg_2, ctg_3
      from goods_category
      where ctg_1 = '식품'
     </select>
     
     <select id="recommendGoods" resultType="vo.GoodsInformVO" parameterType="java.util.HashMap">
        select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img 
      from goods g, event e, shop_code sc, goods_shop gs, goods_category gc 
      where g.good_id = e.good_id
        and sc.shop_code = gs.shop_code
        and gs.good_id = g.good_id 
        and g.good_id = gc.good_id
        and gc.ctg_3=#{ctg_3} 
        and g.good_price between #{min} and #{max}
     </select>
     
     <select id="checkCtg" resultType="vo.GoodsInformVO">
        select ctg_1, ctg_2, ctg_3 
        from goods_category
        where good_id=#{good_id}
     </select>
     
     <select id="countCtg3" resultType="_int">
        select count(good_id)
      from goods_category
      where ctg_3 = #{ctg_3}
     </select>

   <!-- 2020.05.28 추가 -->
   <select id="getNameImg" resultType="vo.GoodsEventShopMemberVO">
      select good_name, good_img, good_id 
      from goods 
      where good_id = #{good_id}
   </select>
   
   <!-- 2020.05.29 추가 -->
   <select id="goodsList_search_paging" resultType="vo.GoodsEventShopMemberVO" parameterType="java.util.HashMap">
      select shop_name, event_name, good_id, good_name, good_price, good_img , search_date, shop_code 
      from (select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_price as good_price, g.good_img as good_img , g.search_date as search_date, sc.shop_code as shop_code, rownum as rnum 
            from goods g, event e, shop_code sc, goods_shop gs
            where g.good_id = e.good_id
              and sc.shop_code = gs.shop_code
              and gs.good_id = g.good_id
              and g.good_name like '%'||#{keyword}||'%')
      where rnum between #{startNum} and #{endNum}
   </select>
   
   <select id="listCount_search" resultType="_int" parameterType="String"> <!-- paging하기 위해 갯수 count (search)-->
        select count(g.good_id) 
        from goods g, event e, shop_code sc, goods_shop gs 
        where g.good_id = e.good_id
        and sc.shop_code=gs.shop_code
        and gs.good_id = g.good_id
        and g.good_name like '%'||#{keyword}||'%'
     </select>
     
     <!-- 2020.05.30 추가 -->
     
     <select id="test" resultType="vo.GoodsInformVO" >
         select sc.shop_name as shop_name, e.event_name as event_name, g.good_id as good_id, g.good_name as good_name, g.good_img as good_img, g.good_price as good_price 
         from goods g, event e, shop_code sc, goods_shop gs, goods_category gc 
         where g.good_id = e.good_id
         and sc.shop_code = gs.shop_code
         and gs.good_id = g.good_id 
         and g.good_id = gc.good_id
         and gc.ctg_3=#{ctg_3}
     </select>
     
</mapper>
```

# dao 전체

```java
package dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.CartVO;
import vo.GoodsEventShopMemberVO;
import vo.GoodsInformVO;

@Repository
public class CartDAO {
   @Autowired
   SqlSession session = null;
   
   //cart담기
   public boolean cartInsert(CartVO cvo) {
      boolean result = false;
      String statement = "resource.CartMapper.insertCart";
      if(session.insert(statement,cvo)==1) {
         result=true;
      }
      return result;
   }
   
   //cart담기 - 2버전 (2020.05.28 수정)
   public boolean cartInsert2(GoodsEventShopMemberVO vo) {
      boolean result = false;
      String statement = "resource.CartMapper.insertCart2";
      if(session.insert(statement,vo)==1) {
         result=true;
      }
      return result;
   }

   //장바구니 비우기
   public boolean cartDelete(String id) {
      boolean result = false;
      String statement = "resource.CartMapper.deleteCart";
      if(session.delete(statement,id)==1) {
         result = true;
      }
      return result;
   }
   
   //장바구니 비우기 - 2버전  (2020.05.28 수정)
   public boolean cartDelete2() {
      boolean result = false;
      String statement = "resource.CartMapper.deleteCart2";
      if(session.delete(statement)>=1) {
         result = true;
      }
      return result;
   }
   //저장된 카트 보여주기
   public List<GoodsEventShopMemberVO> cartView(String id) {
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.selectCart";
      list = session.selectList(statement,id);
      return list;
   }
   
   //상품검색
   public List<GoodsEventShopMemberVO> searchGoods(String keyword){
      List<GoodsEventShopMemberVO> list = new ArrayList<>();
      String statement = "resource.CartMapper.searchGoods";
      list = session.selectList(statement,keyword);
      return list;
   }
   
   //paging(sort)
   public int listCount(String event_name, String shop_code) {
      int count = 0;
      String statement = "resource.CartMapper.listCount";
      if(session.selectOne(statement)!=null) {
         Map<String,String> map = new HashMap<String,String>();
         map.put("event_name", event_name);
         map.put("shop_code", shop_code);
         count = session.selectOne(statement,map);
      }else {
         System.out.println("null이에유");
      }
      return count;
   }
   //상품 전체 리스트 출력
   public List<GoodsEventShopMemberVO> goodsAll(){
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.goodsListAll";
      list = session.selectList(statement);
      //System.out.println(list.get(0));
      return list;
   }
   
   //shopName으로 찾아오기
   public List<GoodsEventShopMemberVO> goodsSortShop(String shop_code) {
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.goodsList_shopName";
      list = session.selectList(statement,shop_code);
      return list;
   }
   
   //eventName으로 찾아오기
   public List<GoodsEventShopMemberVO> goodsSortEvent(String event_name){
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.goodsList_eventName";
      list = session.selectList(statement,event_name);
      return list;
   }
   
   //shopName&eventName 모두로 찾아오기
   public List<GoodsEventShopMemberVO> goodsShopEvent(String event_name, String shop_code){
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.goodsList_shopEvent";
      Map<String,String> map = new HashMap<String,String>();
      map.put("event_name", event_name);
      map.put("shop_code", shop_code);
      //System.out.println(map.keySet());
      list = session.selectList(statement,map);
      //System.out.println("list : "+ list);
      return list;
   }
   
   //shopName&eventName 모두로 찾아오기 + paging
   public List<GoodsEventShopMemberVO> goodsShopEvent(String event_name, String shop_code, int startNum, int endNum){
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.goodsList_shopEvent_paging";
      Map<String,Object> map = new HashMap<String,Object>();
      map.put("startNum",startNum);
      map.put("endNum", endNum);
      map.put("event_name", event_name);
      map.put("shop_code", shop_code);

      list = session.selectList(statement,map);
      //System.out.println("list : "+ list);
      return list;
   }
   
   //2020.05.26 추가
   //ctg_1='식품'인 세부 카테고리 가져오기
   public List<GoodsInformVO> foodsCtg() {
      List<GoodsInformVO> list = new ArrayList<>();
      String statement = "resource.CartMapper.foodsCtg";
      list = session.selectList(statement);
      return list;
   }
   
   //ctg_3에 따른 추천 상품 정보
   public List<GoodsInformVO> recomGoodsList(String ctg_3,int min, int max){
      List<GoodsInformVO> list = new ArrayList<>();
      String statement = "resource.CartMapper.recommendGoods";
      Map<String, Object> map = new HashMap<>();
      map.put("ctg_3",ctg_3);
      map.put("min",min);
      map.put("max",max);
      list = session.selectList(statement,map);
      return list;
   }
   
   //카테고리 체크해줌
   public GoodsInformVO checkCtg(String good_id){
      GoodsInformVO vo = new GoodsInformVO();
      String statement = "resource.CartMapper.checkCtg";
      vo = session.selectOne(statement,good_id);
      return vo;
   }
   
   //ctg_3 갯수 count (Random함수 사용하기 위함)
   public int countCtg3(String ctg_3) {
      String statement = "resource.CartMapper.countCtg3";
      return session.selectOne(statement,ctg_3);
   }
   
   //2020.05.28 추가
   //이름, 이미지 가져옴
   public List<GoodsEventShopMemberVO> getNameImg(String good_id) {
      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
      String statement = "resource.CartMapper.getNameImg";
      list = session.selectList(statement,good_id);
      return list;
   }
   
   //2020.05.29 추가
   //상품검색_paging
   public List<GoodsEventShopMemberVO> searchGoodsPaging(String keyword, int startNum, int endNum){
      List<GoodsEventShopMemberVO> list = new ArrayList<>();
      Map<String,Object> map = new HashMap<String,Object>();
      map.put("startNum",startNum);
      map.put("endNum", endNum);
      map.put("keyword", keyword);
      String statement = "resource.CartMapper.goodsList_search_paging";
      list = session.selectList(statement,map);
      return list;
   }
   
   //paging (search)
   public int listCount2(String keyword) {
      int count = 0;
      String statement = "resource.CartMapper.listCount_search";
      if(session.selectOne(statement)!=null) {
         count = session.selectOne(statement,keyword);
      }else {
         System.out.println("null이에유");
      }
      return count;
   }
   
   //2020.05.30 추가
   public List<GoodsInformVO> test(String ctg_3){
      List<GoodsInformVO> list = new ArrayList<>();
      String statement = "resource.CartMapper.test";
      
      list = session.selectList(statement,ctg_3);
      return list;
   }
}
```

# JSP 전체

```javascript
<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8" import="vo.GoodsVO, vo.CartVO, vo.EventVO, vo.MemberVO,vo.GoodsEventShopMemberVO,java.util.List,java.util.ArrayList"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
   
<!DOCTYPE html>
<html lang="en">
<!-- Basic -->

<head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   
   <!-- Mobile Metas -->
   <meta name="viewport" content="width=device-width, initial-scale=1">
   
   <!-- Site Metas -->
   <title>편의점 마스터, 김편복</title>
   <meta name="keywords" content="">
   <meta name="description" content="">
   <meta name="author" content="">
   
   <!-- Site Icons -->
   <link rel="icon" type="image/png" sizes="16x16"
       href="/pmkim/resources/images/favicon-16x16.png">
   <link rel="shortcut icon" href="/pmkim/resources/images/favicon.ico"
      type="image/x-icon">
   <link rel="apple-touch-icon"
      href="/pmkim/resources/images/apple-touch-icon.png">
   
   <!-- Bootstrap CSS -->
   <link rel="stylesheet" href="/pmkim/resources/css/bootstrap.min.css">
   <!-- Site CSS -->
   <link rel="stylesheet" href="/pmkim/resources/css/style_linda.css">
   <!-- Responsive CSS -->
   <link rel="stylesheet" href="/pmkim/resources/css/responsive.css">
   <!-- Custom CSS -->
   <link rel="stylesheet" href="/pmkim/resources/css/custom.css">
   <link rel="stylesheet" href="/pmkim/resources/css/footerus.css">
   
   <!--[if lt IE 9]>
         <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
         <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
       <![endif]-->

</head>

<body>
   <%
         List<GoodsEventShopMemberVO> gesList = (ArrayList<GoodsEventShopMemberVO>) request.getAttribute("gesList");
   %>
   <!-- Start Main Top -->
   <header class="main-header">
      <!-- Start Navigation -->
      <nav
         class="navbar navbar-expand-lg navbar-light bg-light navbar-default bootsnav">
         <div class="container">
            <!-- Start Header Navigation -->
            <div class="navbar-header">
               <button class="navbar-toggler" type="button" data-toggle="collapse"
                  data-target="#navbar-menu" aria-controls="navbars-rs-food"
                  aria-expanded="false" aria-label="Toggle navigation">
                  <i class="fa fa-bars"></i>
               </button>
               <a class="navbar-brand" href="index.html">
               <img src="/pmkim/resources/images/logo.png" class="logo" alt="">
               </a>
            </div>
            <!-- End Header Navigation -->

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="navbar-menu">
               <ul class="nav navbar-nav ml-auto" data-in="fadeInDown"
                  data-out="fadeOutUp">
                  <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                  <!-- href는 jsp/html 형식이 아닌, {/매핑명}으로  해주시면돼용! 나중에 고쳐주세요~ -->
                  <li class="nav-item"><a class="nav-link" href="map.html">지도</a></li>
                  <!--성진오빠파트-->
                  <li class="dropdown"><a href="#"
                     class="nav-link dropdown-toggle arrow" data-toggle="dropdown">테마</a>
                  <!-- 세호오빠가 원하는 li에다가 href해주세요!-->
                     <ul class="dropdown-menu">
                        <li><a href="shop.html">Sidebar Shop</a></li>
                        <li><a href="shop-detail.html">Shop Detail</a></li>
                        <li><a href="cart.html">Cart</a></li>
                        <li><a href="checkout.html">Checkout</a></li>
                        <li><a href="my-account.html">My Account</a></li>
                        <li><a href="wishlist.html">Wishlist</a></li>
                     </ul></li>
                  <li class="nav-item active"><a class="nav-link"
                     href="event.jsp">행사</a></li>
                  <!-- 지혜파트-->
                  <li class="nav-item"><a class="nav-link" href="mycart.jsp">장바구니</a></li>
                  <!-- 규영언니파트♡ -->
               </ul>
            </div>
            <!-- /.navbar-collapse -->

            <!-- Start Attribute Navigation -->
            <div class="attr-nav">
               <ul>
                  <li class="search"><a href="#"><i class="fa fa-search"></i></a></li>
                  <li class="side-menu"><a href="#"> <i
                        class="fa fa-shopping-bag"></i> <span class="badge">3</span>
                        <p>My Cart</p>
                  </a></li>
               </ul>
            </div>
            <!-- End Atribute Navigation -->
         </div>
   
      </nav>
      <!-- End Navigation -->
   </header>
   <!-- End Main Top -->

   <!-- Start Top Search -->
   <div class="top-search">
      <div class="container">
         <div class="input-group">
            <span class="input-group-addon"><i class="fa fa-search"></i></span>
            <input type="text" class="form-control" placeholder="Search">
            <span class="input-group-addon close-search"><i   class="fa fa-times"></i></span>
         </div>
      </div>
   </div>
   <!-- End Top Search -->

   <!-- Start All Title Box -->
   <div class="all-title-box">
      <div class="container">
         <div class="row">
            <div class="col-lg-12">
               <h2>Shop</h2>
               <ul class="breadcrumb">
                  <li class="breadcrumb-item"><a href="#">Home</a></li>
                  <li class="breadcrumb-item active">Shop</li>
               </ul>
            </div>
         </div>
      </div>
   </div>
   <!-- End All Title Box -->
   
   <!-- Start Shop Page  -->
   <div class="shop-box-inner">
      
      <div class="container">
         <!-- 검색창 -->
         <div class="search-product">
            <form action="/pmkim/cart" method="get">
               <input type="hidden" name="action" value = "search">
               <input class="form-control" name="keyword" placeholder="Search here..." type="text">
               <button type="submit">
                  <i class="fa fa-search"></i>
               </button>
            </form>
         </div>
         <!-- 검색 조건 검색 -->
         <div class="row">
            <div class="col-xl-9 col-lg-9 col-sm-12 col-xs-12 shop-content-right">
               <div class="right-product-box">
                  <form method="GET" action="/pmkim/cart">
                     <div class="product-item-filter row">
                        <div class="col-12 col-sm-8 text-center text-sm-left">
                              <input type ="hidden" name ="action" value = "sort">
                              <div class="toolbar-sorter-right">
                                 <span>편의점 </span> 
                                 <select name="shop_code" class="selectpicker show-tick form-control">
                                    <option value="GS">GS25</option>
                                    <option value="CU">CU</option>
                                    <option value="MS">ministop</option>
                                    <option value="SE">7eleven</option>
                                    <option value="EM">emart24</option>
                                 </select>
                              </div>
                              <br>
                              <br>
                              <div class="toolbar-sorter-right">
                                 <span>행사 종류</span> 
                                 <select name="event_name" class="selectpicker show-tick form-control">
                                    <option value="1+1">1+1</option>
                                    <option value="2+1">2+1</option>
                                    <option value="SALE">Sale</option>
                                    <option value="Fresh Food">FreshFood</option>
                                    <option value="PB">PB</option>
                                 </select>
                              </div>
                              
                           <!-- <p>Showing all 4 results</p> -->
                        </div>
                        <div class="col-12 col-sm-4 text-center text-sm-right">
                           <ul class="nav nav-tabs ml-auto">
                              <li><a class="nav-link active" href="#grid-view"
                                 data-toggle="tab"> <i class="fa fa-th"></i>
                              </a></li>
                              <li><a class="nav-link" href="#list-view"
                                 data-toggle="tab"> <i class="fa fa-list-ul"></i>
                              </a></li>
                           </ul>
                           <button type="submit">
                              <i class="fa fa-search"></i>
                           </button>
                        </div>
                  </div>
               </form>
                  
                  <div class="product-categorie-box">
<!--                      <form method="GET" action="/pmkim/happy" id="listform" name="listform">
 -->                     <div class="tab-content">
                        <div role="tabpanel" class="tab-pane fade show active"
                           id="grid-view">
                           <div class="row">
                           <!-- 상품출력 반복문 -->
                           <c:forEach var="vo" items="${ gesList }" varStatus="status">
                              <div class="col-sm-6 col-md-6 col-lg-4 col-xl-4">
                                 <div class="products-single fix">
                                    <div class="box-img-hover">
                                       <div class="type-lb">
                                          <p class="sale">${ vo.shop_name }</p>
                                       </div>
                                       <img src= "${ vo.good_img }" class="img-fluid" alt="Image">
                                       <div class="mask-icon">
                                          <a class="cart" onclick="add('${vo.good_id}'); return false;">Add</a>
                                       </div>
                                    </div>
                                    <div class="why-text">
                                       <input type="hidden" name="good_id" value="${ vo.good_id }" class="good_id">
                                       <h4 class="good_name">${ vo.good_name }</h4>
                                       <h5 class="good_price">${ vo.good_price }원</h5>
                                       <h5 class="event_name">${ vo.event_name }</h5>
                                    </div>
                                 </div>
                              </div>
                           </c:forEach>
                           </div>
                        </div>
                     </div>
<!--                      </form>                              
 -->                     
                     <!-- start paging -->
                     <div id="paging" style="text-align : center; font-size : 16pt;">
                        <c:if test="${ preData }">
                           <a href ="/pmkim/cart?pgNum=1${ oldQ }"> &laquo; </a>
                           <a href = "/pmkim/cart?pgNum=${ pgNum - 1 }${ oldQ }"> &nbsp; &lt; &nbsp;</a>
                        </c:if>
                        
                        <c:forEach var="num" begin="${ pageStart }" end="${ pageEnd }">
                           <a href = "/pmkim/cart?pgNum=${ num }${ oldQ }">${ num } &nbsp;</a>
                        </c:forEach>
                        
                        <c:if test="${ nextData }">
                           <a href = "/pmkim/cart?pgNum=${ pgNum + 1 }${ oldQ }"> &gt; &nbsp;</a>
                        </c:if>
                        
                        <c:if test = "${ pgNum != end }">
                        <a href ="/pmkim/cart?pgNum=${ end }${ oldQ }"> &raquo; </a>
                        </c:if>
                     </div>
                     <!-- end paging -->
                  </div>
               </div>
            </div>
            
            <div class="col-xl-3 col-lg-3 col-sm-12 col-xs-12 sidebar-shop-left">
            <!-- 여기에 만원의 행복 들어옴!! -->
               <div class="product-categori">
                  
                  
                     <div class="list-group list-group-collapse list-group-sm list-group-tree" id="list-group-men" data-children=".sub-men">
                        <div class="filter-price-left">
                                  <div class="title-left">
                                      <h3>Price</h3>
                                  </div>
                                  <div class="price-box-slider">
                                      <div id="slider-range"></div>
                                      <p>
                                          <input type="text" id="amount" readonly style="border:0; color:#fbb714; font-weight:bold;">
                                          <button class="btn hvr-hover" onclick="recommend(); return false;">Filter</button>
                                          <button class="btn hvr-hover" onclick="deleteCart(); return false;">Reset</button>                                          
                                      </p>
                                      <div id ="cart-View" class="list-group-collapse sub-men">
                                        상품을 클릭하세요.
                                     <!-- 담은 상품 여기에 나타내기  = add함수의 결과 여기로 가져옴 -->
                                     </div>
                                  </div>
                                  
                              </div>
                     </div>
               </div>
            </div>
         </div>
      </div>
   </div>
   <!-- End Shop Page -->

   <!-- 20200521_oliver.yoo -->
   <!-- Start Footer  -->
   <footer>
      <div class="footer-main">
         <div class="container">
            <div class="row">

               <div class="col-lg-4 col-md-12 col-sm-12">
                  <div class="footer-top-box">
                     <h3>챗봇(Coming Soon)</h3>

                  </div>
               </div>

            </div>
            <hr>

            <div class="container text-centers">
               <div class="row">
                  <!-- Footer 1-->
                  <div class="col-lg-422 mb-5 mb-lg-0">
                     <a><img src="/pmkim/resources/images/haley2.png" class="profile"  alt="" /></a>
                  <h2>Haley Oh</h2>
                  <a href="https://github.com/JihyeHaley"><img src="/pmkim/resources/images/gitprof.png" class="git_img"/></a> 
                  </div>

                  <!-- Footer 2-->
                  <div class="col-lg-422 mb-5 mb-lg-0">
                     <a><img src="/pmkim/resources/images/seho2.png" class="profile"   alt="" /></a>
                  <h2>Seho Oh </h2>
                  <a href="https://github.com/sehooh5"><img src="/pmkim/resources/images/gitprof.png" class="git_img"/></a> 
                  </div>

                  <!-- Footer 3-->
                  <div class="col-lg-422 mb-5 mb-lg-0">
                     <a><img src="/pmkim/resources/images/linda2.png" class="profile" alt="" /></a>
                     <h2>Linda Eom </h2>
                     <a href="https://github.com/GyuyoungEom"><img src="/pmkim/resources/images/gitprof.png" class="git_img"/></a>
                  </div>

                  <!-- Footer 4-->
                  <div class="col-lg-422 mb-5 mb-lg-0">
                     <a><img src="/pmkim/resources/images/oliver2.png" class="profile"  /></a>
                     <h2>Oliver Yoo </h2>
                     <a href="https://github.com/SeongjinOliver"><img src="/pmkim/resources/images/gitprof.png" class="git_img"/></a>
                  </div>
               </div>
            </div>


            <div class="row">
               <div class="col-lg-4 col-md-12 col-sm-12">
                  <div class="footer-widget">
                     <h4>About 편마 김편복</h4>
                     <p>편의점 마스터! 김편복  데이터, 위치기반을 활용한 편의점 상품 추천 서비스</p>
                     <p>편의점에서 점심을 간단히 먹고 싶은 김편복씨는 자신의 위치에서 먹고자하는  상품 어느 편의점에서 행사를 하는지 알고 싶은데 알 수 있는 방법이 없다!! 이럴때 필요한 서비스는 "<b>편마 김편복</b>"</p>
                  </div>
               </div>
               <div class="col-lg-4 col-md-12 col-sm-12">
                  <div class="footer-link">
                     <h4>Information</h4>
                     <ul>
                        <li><a href="#/pmkim/main">HOME</a></li>
                        <li><a href="#/pmkim/map">지도</a></li>
                        <li><a href="#/pmkim/theme">테마</a></li>
                        <li><a href="#/pmkim/event">행사</a></li>
                        <li><a href="#/pmkim/cart">장바구니</a></li>
                        <li><a href="#/pmkim/mypage">마이페이지</a></li>
                     </ul>
                  </div>
               </div>
               <div class="col-lg-4 col-md-12 col-sm-12">
                  <div class="footer-link-contact">
                     <h4>Contact Us</h4>
                     <ul>
                        <li>
                           <p>
                              <i class="fas fa-map-marker-alt"></i>
                                    주소: 서울특별시 강남구 테헤란로 212 <br>(역삼동 718-5번지)<br> (우) 06220
                           </p>
                        </li>
                        <li>
                           <p>
                              <i class="fas fa-phone-square"></i>Phone: <a
                                 href="tel:+81-1029852154">+82-10 2985 2154</a>
                           </p>
                        </li>
                        <li>
                           <p>
                              <i class="fas fa-envelope"></i>Email: <a
                                 href="mailto:ohhojh@gmail.com">ohhojh@gmail.com</a>
                           </p>
                        </li>
                     </ul>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </footer>
   <!-- End Footer  -->
   <!-- Start copyright  -->
   <div class="footer-copyright">
      <p class="footer-company">
         All Rights Reserved. &copy; 2018 <a href="#">ThewayShop</a> Design By
         : <a href="https://html.design/">html design</a>
      </p>
   </div>
   <!-- End copyright  -->
   <a href="#" id="back-to-top" title="Back to top" style="display: none;">&uarr;</a>

   <!-- ALL JS FILES -->
   <script src="/pmkim/resources/js/jquery-3.2.1.min.js"></script>
   <script src="/pmkim/resources/js/popper.min.js"></script>
   <script src="/pmkim/resources/js/bootstrap.min.js"></script>
   <!-- ALL PLUGINS -->
   <script src="/pmkim/resources/js/jquery.superslides.min.js"></script>
   <script src="/pmkim/resources/js/bootstrap-select.js"></script>
   <script src="/pmkim/resources/js/inewsticker.js"></script>
   <script src="/pmkim/resources/js/bootsnav.js"></script>
   <script src="/pmkim/resources/js/images-loded.min.js"></script>
   <script src="/pmkim/resources/js/isotope.min.js"></script>
   <script src="/pmkim/resources/js/owl.carousel.min.js"></script>
   
   <script src="/pmkim/resources/js/baguetteBox.min.js"></script>
   <script src="/pmkim/resources/js/jquery-ui.js"></script>
   <script src="/pmkim/resources/js/jquery.nicescroll.min.js"></script>
   <script src="/pmkim/resources/js/form-validator.min.js"></script>
   <script src="/pmkim/resources/js/contact-form-script.js"></script>
   <script src="/pmkim/resources/js/custom_linda.js"></script>
   <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

   <!-- custom js -->
   <script>
      function recommend(){         
         //클릭한 아이템 받아오기
         //그 아이템에 대해서 추천 아이템 가져오기
         //var good_id = document.getElementByClassName('good_id');
         console.log(document.getElementById('selectId'));
         
         $.ajax({
            type :"get",// 전송 방식 
            url :"/pmkim/happy",  //컨트롤러 사용할 때. 내가 보낼 데이터의 주소. 
            data : {"good_id" : document.getElementById('selectId').value,
                  "minM" : $('#amount').val().split('-')[0].replace('원',"")*1,
                  "maxM" : $('#amount').val().split('-')[1].replace('원',"")*1
                  },
            dataType : "json",   // text, xml, html, script, json, jsonp 가능 
            success : function(data){   
               if(data=="1"){
                  alert("추천");
               }else{
                  alert("추천 상품이 없습니다.");
               }
            },
            error : function(){
               alert("프로그램 에러가 발생했습니다.");
            }
            //console.log(document.querySelector("#cart-View > img"));
         });
         
         var x = $('#amount').val().split('-')[0].replace('원',"")*1;
         console.log(x);
         //console.log($('#slider-range').slide());   

      }
      
      //클릭 상품 저장
      function add(good_id){
         $.ajax({
            type :"post",
            url :"/pmkim/cart",  
            data : {"action" : "insert",
                  "good_id" : good_id},
            dataType : "json",   // text, xml, html, script, json, jsonp 가능 
            //async : false,
            success : function(data){   
               if(data=="1"){

                  var key = [];         //id값 담을 변수 선언
                  var num = document.getElementsByClassName('good_id').length
                  for(var i=0; i<num; i++){
                     key[i] = document.getElementsByClassName('good_id')[i].value;
                  }
                  var good_name = document.getElementsByClassName('good_name')[key.indexOf(good_id)].innerHTML;
                  var good_img = document.getElementsByClassName('img-fluid')[key.indexOf(good_id)].getAttribute('src');

                  document.getElementById('cart-View').innerHTML = "<p id='result_name'>"+ good_name + "</p> <br>"+"<img src = '"+good_img+"' class ='img-fluid'>"
                                                      +"<input type='hidden' value = '"+good_id+"' id = 'selectId' name='selectId'>";

               }else{
                  alert("상품이 선택되지 않았습니다.");
               }
            },
            error : function(){
               alert("프로그램 에러가 발생했습니다.");
            }
         });
         
      }
      
      //클릭상품 해제
      function deleteCart(){
         $.ajax({
            type :"post",// 전송 방식 
            url :"/pmkim/cart",  //컨트롤러 사용할 때. 내가 보낼 데이터의 주소. 
            data : {"action" : "delete"},
            dataType : "json",   // text, xml, html, script, json, jsonp 가능 
            success : function(data){   
               if(data=="1"){
                  document.getElementById('cart-View').innerHTML = '상품을 클릭하세요.';
               }else{
                  alert("선택한 상품이 없습니다.");
               }
            },
            error : function(){
               alert("프로그램 에러가 발생했습니다.");
            }
         });
      }
   </script>
   
</body>

</html>
```

