# 개발 일지(Login Fail)

I have to other reference.

#### JPA설정 방법

- pom.xml

```xml
<!-- https://mvnrepository.com/artifact/org.eclipse.persistence/org.eclipse.persistence.jpa -->
<dependency>
<groupId>org.eclipse.persistence</groupId>
<artifactId>org.eclipse.persistence.jpa</artifactId>
<version>2.5.2</version>
</dependency>
```

@Entity 어노테이션을 사용할 수 있게 해준다.

- @NotEmpty

```xml
<dependency>
<groupId>javax.validation</groupId>
<artifactId>validation-api</artifactId>
<version>1.1.0.Final</version>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-validator</artifactId>
<version>5.1.3.Final</version>
</dependency>
```
- @CookieValue Annotation을 이용하면 쿠키 값을 파라미터로 전달받을 수 있다.

  

  @CookieValue Annotation은 해당 쿠키가 존재하지 않으면 기본적으로 500 에러를 발생시킨다. 따라서, 쿠키가 필수가 아닌 경우에는 required 속성의 값을 false로 지정해 주어야 한다. required 속성의 기본 값은 true이다.

  required 속성의 값을 false로 지정할 경우, 해당 쿠키가 존재하지 않으면 null을 값으로 전달받게 된다.

#### WeetCustomerinfoVO.java

```java
package vo;

import javax.persistence.Entity;
import org.hibernate.validator.constraints.NotEmpty;

@Entity
public class WeetCustomerInfoVO {
	
	@NotEmpty(message="아이디를 입력해주세요")
	private String customer_id;
	@NotEmpty(message="비밀번호를 입력해주세요.")
	private String customer_pwd;
	private String customer_name;
	private String customer_phone;
	private String customer_addr;
	private String customer_nickname;
	private int customer_rank;
	private String customer_date;
	private String customer_kindof_login;
	private boolean rememberId;
	
    public boolean getRememberId() {
        return rememberId;
    }
    public void setRememberId(boolean rememberId) {
        this.rememberId = rememberId;
    }
	
	public String getCustomer_kindof_login() {
		return customer_kindof_login;
	}
	public void setCustomer_kindof_login(String customer_kindof_login) {
		this.customer_kindof_login = customer_kindof_login;
	}
	public String getCustomer_id() {
		return customer_id;
	}
	public void setCustomer_id(String customer_id) {
		this.customer_id = customer_id;
	}
	public String getCustomer_pwd() {
		return customer_pwd;
	}
	public void setCustomer_pwd(String customer_pwd) {
		this.customer_pwd = customer_pwd;
	}
	public String getCustomer_name() {
		return customer_name;
	}
	public void setCustomer_name(String customer_name) {
		this.customer_name = customer_name;
	}
	public String getCustomer_phone() {
		return customer_phone;
	}
	public void setCustomer_phone(String customer_phone) {
		this.customer_phone = customer_phone;
	}
	public String getCustomer_addr() {
		return customer_addr;
	}
	public void setCustomer_addr(String customer_addr) {
		this.customer_addr = customer_addr;
	}
	public String getCustomer_nickname() {
		return customer_nickname;
	}
	public void setCustomer_nickname(String customer_nickname) {
		this.customer_nickname = customer_nickname;
	}
	public int getCustomer_rank() {
		return customer_rank;
	}
	public void setCustomer_rank(int customer_rank) {
		this.customer_rank = customer_rank;
	}
	public String getCustomer_date() {
		return customer_date;
	}
	public void setCustomer_date(String customer_date) {
		this.customer_date = customer_date;
	}
}
```

#### WeetController.java

```java
package my.spring.weet;

import javax.servlet.http.Cookie;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import dao.WeetMybatisDAO;
import vo.WeetCustomerInfoVO;

@Controller
public class WeetController {
	@Autowired
	WeetMybatisDAO dao;

	 @RequestMapping(value="/login", method=RequestMethod.GET)
    public ModelAndView loginForm(WeetCustomerInfoVO customVO, String action,
                    @CookieValue(value="REMEMBER", required=false) Cookie rememberCookie) throws Exception {

		ModelAndView mav = new ModelAndView();
        //ModelAndView mv = new ModelAndView("user/login");
		String showView = "";

		showView = "login_";
        if(rememberCookie!=null) {
        	customVO.setCustomer_id(rememberCookie.getValue());
       	customVO.setRememberId(true);
        }
      
       

        mav.setViewName(showView);
        return mav;
    }	
}
```



#### login_.jsp

```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Login</title>
</head>
<body>
<div class="panel-body">
   <form action="/login" method="post">
        <fieldset>
            <div class="form-group">
                <!-- <form:input type="text" class="form-control" placeholder="ID" path="id"/> -->
                <input id='userid' type='text' placeholder="ID"/>
            </div>
            <div class="form-group">
                 <!-- <form:password class="form-control" placeholder="Password" path="pw"/> -->
                 <input id='pwd' type='password' placeholder="Password"/>
            </div>
            <div class="checkbox">
                <label>
                    <!-- <form:checkbox path="rememberId"/>아이디 기억 -->
                    	
					<input type="checkbox" name="rememberId">아이디 기억
                </label>
            </div>
                <button type="submit" class="btn btn-lg btn-success btn-block">로그인</button>
        </fieldset>
    </form>
</div>

</body>
</html>
```

#### AuthInfoVO.java

```java
package vo;

//회원 정보 세션 유지
public class AuthInfoVO {
  
  private String id;
  private String name;
  private int grade;
  
  public AuthInfoVO(String id, String name, int grade) {
      this.id = id;
      this.name = name;
      this.grade = grade;
  }
  
  public String getId() {
      return id;
  }
  public void setId(String id) {
      this.id = id;
  }
  public String getName() {
      return name;
  }
  public void setName(String name) {
      this.name = name;
  }
  public int getGrade() {
      return grade;
  }
  public void setGrade(int grade) {
      this.grade = grade;
  }

}
```

회원 정보 세션을 유지해주는 기능을 할 것이다. UserVO를 그대로 사용하게 되면 보안성에 취약할 뿐만 아니라, 불필요한 정보까지 유지가 된다. 그래서 따로 세션 정보 유지를 위해 만들었다.

\- 10~14행 : 로그인이 성공하면서, 저장된다

#### UserVO.java

```java
package tody.lovely.vo;
 
import java.util.Date;
 
public class UserVO {
    
    private int IDX;
    private String ID;
    private String EMAIL;
    private String NAME;
    private String PASSWORD;
    private int GRADE;
    private Date REGDATE;
        
    //비밀번호 확인
    public boolean matchPassword(String pw) {
        return this.PASSWORD.equals(pw);
    }
 
    /* Getter, Setter 생략 */
}
```

\- 16~18행 : 비밀번호 확인을 위해서 추가했다.

