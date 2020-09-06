# binary search



정렬 되어 있는 숫자들 중에서 특정 숫자를 찾는다. O(nlogn)

중복값이 없을 때 검색 가능한 알고리즘이다.

```java
void binSearch(int s, int e) {
	if (s + 1 >= e) {
		minRes = e;
		return;
	}
	isOk = false;
	mid = (s + e) / 2;
	recur(0, 0);
	if (isOk) binSearch(s, mid);
	else binSearch(mid, e);
}
```

