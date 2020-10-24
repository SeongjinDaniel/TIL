# Calendar



```java
public static void main(String[] args) {
    Calendar cal = null;
    Calendar from = Calendar.getInstance();
    Calendar to = Calendar.getInstance();
    from.add(Calendar.DATE, -CommonKeys.DAYS_180); // from 180 days ago

    //cal = histQuote.getDate();
    format = new SimpleDateFormat("yyyy-MM-dd");
    formatted = format.format(cal.getTime()); // ex) Output "2020-10-21"
}

```

