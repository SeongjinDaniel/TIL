# Spring Day2

### 예제 sample 6

-----------

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:c="http://www.springframework.org/schema/c"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="messageBean" class="sample6.MessageBeanImpl"
      c:name="Dooly"   p:outputter-ref="outputRef"  
      p:phone="123-4567" />
<bean id="outputRef" class="sample6.FileOutput"  
      p:filePath="data.txt"/>

<!-- <bean id="messageBean" class="sample6.MessageBeanImpl">
	<constructor-arg  value="Dooly"/>	
	<property name="phone"  value="123-4567"/>
	<property name="outputter" ref="outputRef"/>
</bean>

<bean id="outputRef" class="sample6.FileOutput">
	<property name="filePath">
		<value>data.txt</value>
	</property>
</bean> -->

</beans>
```

```java
package sample6;

import java.io.IOException;

public class MessageBeanImpl implements MessageBean{
	private String name;
	private String phone;
	private Outputter outputter;
	
	//생성자로 name을 받음
	public MessageBeanImpl(String name) {
		super();
		this.name = name;
		System.out.println("1. Bean Constructor Call");
	}
	
	//setter을 통해서 phone와 outputter입력받음
	public void setPhone(String phone) {
		this.phone = phone;
		System.out.println("4. phone's info set");
	}
	
	public void setOutputter(Outputter outputter) {
		this.outputter = outputter;
		System.out.println("3. outputter's info set");
	}

	@Override
	public void helloCall() {
		String message=name+" : " +phone;
		System.out.println("helloCall() : "+message);
		
		try {
			outputter.output(message);
			System.out.println("6. Finish");
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
```

```java
package sample6;

public interface MessageBean {
	public void helloCall();
}
```

```java
package sample6;

import java.io.FileWriter;
import java.io.IOException;

public class FileOutput implements Outputter{
	private String filePath;  
	
	public void setFilePath(String filePath) {
		this.filePath = filePath;
		System.out.println("2. File's info set");
	}

	@Override
	public void output(String message) throws IOException {
		FileWriter out=new FileWriter(filePath);
		out.write(message);
		out.close();
		System.out.println("5. Writing successful");
	}
}
```

```java
package sample6;

import java.io.IOException;

public interface Outputter {
	public void output(String message) throws IOException;
}
```

```java
package sample6;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloSpringApp {
	public static void main(String[] args) {
		ApplicationContext factory
        		= new ClassPathXmlApplicationContext("sample6/applicationContext.xml");

		System.out.println("** Container Initialization End **");
		MessageBean bean=(MessageBean)factory.getBean("messageBean");
		bean.helloCall();

		((ClassPathXmlApplicationContext) factory).close();
	}
}
```

------

#### 예제 sample7

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="developer" class="sample7.Developer">
	<constructor-arg value="dooly"/>
	<constructor-arg value="1500000"/>
	<property name="dept"   value="Development 1 Team"/>
</bean>

<bean id="engineer" class="sample7.Engineer">
	<constructor-arg   value="duke"/>
	<constructor-arg   value="2500000"/>
	<property name="dept"   value="Technology 1 Team"/>	
</bean>

</beans>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:c="http://www.springframework.org/schema/c"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="developer" class="sample7.Developer" 
    c:name="Dooly" c:salary="1500000"    p:dept="Development 1 Team"/> <!-- name, salary는 매개변수, dept는 set생략후 첫글자 소문자 -->
<bean id="engineer" class="sample7.Engineer" 
    c:name="Duke" c:salary="2500000"    p:dept="Technology 1 Team"/>
</beans>
```

```java
package sample7;

public class Emp {
	private String name;
	private int salary;
	
	public Emp() {
		super();
	}
	public Emp(String name, int salary) {
		super();
		this.name = name;
		this.salary = salary;
	}
	@Override
	public String toString() {
		return "Name : " + name + ", Salary : " + salary + ", ";
	}
}
```

```java
package sample7;

public class Developer extends Emp{
	private String dept;
	
	public Developer() {
		super();
	}

	public Developer(String name, int salary) {
		super(name, salary);
	}

	public void setDept(String dept) {
		this.dept = dept;
	}

	@Override
	public String toString() {
		return super.toString() + " Department : " + dept;
	}
}
```

```java
package sample7;

public class Engineer extends Emp{
	private String dept;

	public Engineer() {
		super();
	}

	public Engineer(String name, int salary) {
		super(name, salary);
	}

	public void setDept(String dept) {
		this.dept = dept;
	}

	@Override
	public String toString() {
		return super.toString() + " Department : " + dept;
	}
}
```

```java
package sample7;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class EmpMain {
	public static void main(String[] args) {
		ApplicationContext factory =
				   new ClassPathXmlApplicationContext("sample7/bean1.xml");
		
		Emp b1 = (Emp)factory.getBean("developer");
		System.out.println(b1.toString());
		
		Emp b2 = (Emp)factory.getBean("engineer");
		System.out.println(b2.toString());
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

----

#### 실습7 sample8

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!-- 생성자를 통한 객체 생성 -->
<bean id="developer" class="sample8.Developer">
	<constructor-arg name="emp"  ref="emp1" />
	<constructor-arg name="dept"  value="Development 1 Team"/>
</bean>
<bean id="engineer" class="sample8.Engineer">
	<constructor-arg name="emp"  ref="emp2" />
	<constructor-arg name="dept"  value="Technology 1 Team"/>
</bean>

<bean id="emp1" class="sample8.Emp">
	<constructor-arg name="name"  value="Dooly"/>
	<constructor-arg name="salary"  value="1500000"/>
</bean>
<bean id="emp2" class="sample8.Emp">
	<constructor-arg name="name"  value="Duke"/>
	<constructor-arg name="salary"  value="2500000"/>
</bean>
</beans>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:c="http://www.springframework.org/schema/c"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!-- How to set properties using XML namespace -->
<bean id="developer" class="sample8.Developer"  
        					c:_0-ref="emp1"  c:_1="Development 1 Team"/> <!-- 이름-ref 또다른 빈객체의 참조값을 전달 , _0 : 첫번째 매개변수 , _1 두번째 매개변수 -->
<bean id="engineer" class="sample8.Engineer"   
        					c:emp-ref="emp2"  c:dept="Technology 1 Team"/>

<bean id="emp1"  class="sample8.Emp" 
                           	c:_0="Dooly" c:_1="1500000"/>
<bean id="emp2"  class="sample8.Emp" 
							c:name="Duke" c:salary="2500000"/>
</beans>
```

```java
package sample8;

public class Emp {
	private String name;
	private int salary;
	
	public Emp() {
		super();
	}
	public Emp(String name, int salary) {
		super();
		this.name = name;
		this.salary = salary;
	}
	@Override
	public String toString() {
		return "Name : " + name + ", Salary : " + salary + ", ";
	}
}
```

```java
package sample8;

public class Developer{
	private Emp emp;
	private String dept;
	
	public Developer() {
		super();
	}
	public Developer(Emp emp, String dept) {
		super();
		this.emp = emp;
		this.dept = dept;
	}
	@Override
	public String toString() {
		return emp.toString() + " Department : " + dept;
	}
}
```

```java
package sample8;

public class Engineer{
	private Emp emp;
	private String dept;

	public Engineer() {
		super();
	}
	public Engineer(Emp emp, String dept) {
		super();
		this.emp = emp;
		this.dept = dept;
	}
	@Override
	public String toString() {
		return emp.toString() + " Department : " + dept;
	}
}
```

```java
package sample8;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class EmpMain {
	public static void main(String[] args) {
		ApplicationContext factory =
				   new ClassPathXmlApplicationContext("sample8/bean2.xml");
		
		Developer b1 = (Developer)factory.getBean("developer");
		System.out.println(b1.toString());
		
		Engineer b2 = (Engineer)factory.getBean("engineer");
		System.out.println(b2.toString());
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

autowire="byName"  : setter
(1) 프로퍼티명과 동일한 명칭의 빈을 찾아서 해당 객체 주입
(2) 없으면 null 주입

autowire="byType"  : setter
(1) 매개변수 타입으로 찾아서 1개이면 해당 객체 주입
(2) 매개변수 타입으로 찾아서 2개 이상이면 NoUniqueBeanDefinitionException 발생
(3) 없으면 null 주입

autowire="constructor"  : constructor
(1) 타입으로 찾아서 1개이면 해당 객체 주입
(2) 타입으로 찾아서 2개 이상이면 매개변수명과 동일한 id 값을 갖는 객체 주입
(3) 없으면 null 주입

#### 예제 sampleanno01

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<bean id="user"  class="sampleanno01.User">
	<property name="name" value="Dooly"/>
	<property name="age"  value="10"/>
	<property name="hobby" value="swimming"/>
</bean>

<bean id="myProcess0"  class="sampleanno01.UserShow" /> <!-- no 아규먼트 생성자 호출 -->
<bean id="myProcess1"  class="sampleanno01.UserShow"  
										autowire="byName"/> <!-- 이름을 객체를 찾아서 설정해줘! 알아서 셋터 메 --> <!-- byName : 소문자 user라는 이름으로 만들어진 객체를 알아서 셋팅해줘(setter 메서드) -->
<bean id="myProcess2"  class="sampleanno01.UserShow"  
										autowire="byType"/> <!-- byType : user라는 타입에 알맞는것이 있으면 자동으로 넣어줘(setter 메서드) -->
<bean id="myProcess3"  class="sampleanno01.UserShow"  
										autowire="constructor"/> <!-- constructor : 생성자를 호출해서 넣어줘 -->

</beans>
```

```java
package sampleanno01;

public class User {
	private String name;
	private int age;	
	private String hobby;

	public void setName(String name) {
		this.name = name;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public void setHobby(String hobby) {
		this.hobby = hobby;
	}

	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public String getHobby() {
		return hobby;
	}

	@Override
	public String toString() {
		return "User [name=" + name + ", age=" + age + ", hobby=" + hobby + "]";
	}
}
```

```java
package sampleanno01;

public class UserShow {
	private User user;

	public UserShow() {
		super();
		System.out.println("Constructor Call(no-args)");
	}
	public UserShow(User user) {
		super();
		this.user = user;
		System.out.println("Constructor Call(User-args)");
	}
	
	public void setUser(User user1) {
		System.out.println("Setter Call by Autowire");
		this.user = user1;
	}

	@Override
	public String toString() {
		return "UserShow [user=" + user + "]";
	}

}
```

```java
package sampleanno01;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class UserMain {

	public static void main(String[] args) {
		ApplicationContext factory 
		    = new ClassPathXmlApplicationContext("sampleanno01/bean.xml");
		System.out.println("**** Container Initialization End ****");		
		UserShow ob=factory.getBean("myProcess0", UserShow.class);
		System.out.println(ob.toString());	
		System.out.println("-----------------");		
		UserShow ob1=factory.getBean("myProcess1", UserShow.class);
		System.out.println(ob1.toString());	
		System.out.println("-----------------");		
		UserShow ob2=factory.getBean("myProcess2", UserShow.class);
		System.out.println(ob2.toString());	
		System.out.println("-----------------");		
		UserShow ob3=factory.getBean("myProcess3", UserShow.class);
		System.out.println(ob3.toString());	
		
		((ClassPathXmlApplicationContext)factory).close();
	}
}
```

-------

#### 예제 sampleanno02

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!-- 테스트1 -->
<!-- 
<bean id="myFood" class="sampleanno02.MyFoodMgr">
	<property name="favoriteFood" ref="favoriteFood"/>
	<property name="unFavoriteFood" ref="unFavoriteFood"/>
</bean>

<bean id="favoriteFood" class="sampleanno02.Food" >
	<property name="foodName" value="Bread"/>
	<property name="foodPrice" value="1500"/>
</bean>
<bean id="unFavoriteFood" class="sampleanno02.Food" >
	<property name="foodName" value="Noodle"/>
	<property name="foodPrice" value="2500"/>
</bean> -->

<!-- 테스트2 -->
<bean id="myFood" class="sampleanno02.MyFoodMgr" autowire="constructor"/>

<bean id="favoriteFood" class="sampleanno02.Food" >
	<property name="foodName" value="Noodle"/>
	<property name="foodPrice" value="2500"/>
</bean>
<bean id="unFavoriteFood" class="sampleanno02.Food" >	
	<property name="foodName" value="Bread"/>
	<property name="foodPrice" value="1500"/>
</bean>
</beans>

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean id="myFood" class="sampleanno02.MyFoodMgr" autowire="byName"/>
<bean id="favoriteFood" class="sampleanno02.Food" p:foodName="Bread" p:foodPrice="1500"/>
<bean id="unFavoriteFood" class="sampleanno02.Food" p:foodName="Noodle" p:foodPrice="2500"/>
</beans>

```

```java
package sampleanno02;

//setter, toString()추가
public class MyFoodMgr{
	private Food favoriteFood;
	private Food unFavoriteFood;	
	
	public MyFoodMgr() {}
	public MyFoodMgr(Food favoriteFood, Food unFavoriteFood) {
		super();
		this.favoriteFood = favoriteFood;
		this.unFavoriteFood = unFavoriteFood;
		System.out.println(favoriteFood);
		System.out.println(unFavoriteFood);
	}
	public void setFavoriteFood(Food favoriteFood) {
		this.favoriteFood = favoriteFood;
	}
	public void setUnFavoriteFood(Food unFavoriteFood) {
		this.unFavoriteFood = unFavoriteFood;
	}
	@Override
	public String toString() {
		return "[Food1=" + favoriteFood + ", Food2=" + unFavoriteFood + "]";
	}
}
```

```java
package sampleanno02;

public class Food {
	private String foodName;
	private int foodPrice;
	
	public void setFoodName(String foodName) {
		this.foodName = foodName;
	}
	public void setFoodPrice(int foodPrice) {
		this.foodPrice = foodPrice;
	}
	@Override
	public String toString() {
		return "Food [foodName=" + foodName + ", foodPrice=" + foodPrice + "]";
	}
}
```

```java
package sampleanno02;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class FoodTest {
	public static void main(String[] args) {
		ApplicationContext factory = 
				new ClassPathXmlApplicationContext("sampleanno02/bean1.xml");

		System.out.println("-------------1");
		MyFoodMgr ob=factory.getBean("myFood", MyFoodMgr.class);
		System.out.println("-------------2");
		System.out.println(ob.toString());

		((ClassPathXmlApplicationContext) factory).close();
	}
}
```

