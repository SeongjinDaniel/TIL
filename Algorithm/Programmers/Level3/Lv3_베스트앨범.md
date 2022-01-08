# Lv3_베스트앨범



#### Mine

```java
import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        List<Integer> answerList = new ArrayList<>();
        Map<String, Integer> hmGenres = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            hmGenres.put(genres[i], hmGenres.getOrDefault(genres[i], 0) + plays[i]);
        }
        
        
        // 1. 장르
        List<String> genreList = new ArrayList<>(hmGenres.keySet());
        Collections.sort(genreList, (o1, o2) -> (hmGenres.get(o2).compareTo(hmGenres.get(o1))));

        // 2. 노래
        for (String genre : genreList) {
            Map<Integer, Integer> hmIndex = new HashMap<>();
            for(int i = 0; i < plays.length; i++) {
                if (genre.equals(genres[i])) {
                    hmIndex.put(i, plays[i]);
                }
            }
            List<Integer> indexList = new ArrayList<>(hmIndex.keySet());
            indexList.sort((o1, o2) -> hmIndex.get(o2).compareTo(hmIndex.get(o1)));
            for (int i = 0; i < indexList.size(); i++) {
                if (i >= 2) {
                    break;
                }
                answerList.add(indexList.get(i));
            }
        }
        answer = answerList.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
}
```



#### Others

```java
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
  public class Music implements Comparable<Music>{

    private int played;
    private int id;
    private String genre;

    public Music(String genre, int played, int id) {
      this.genre = genre; 
      this.played = played;
      this.id = id;
    }

    @Override
    public int compareTo(Music other) {
      if(this.played == other.played) return this.id - other.id;
      return other.played - this.played;
    }

    public String getGenre() {return genre;}
  }

  public int[] solution(String[] genres, int[] plays) {
    return IntStream.range(0, genres.length)
    .mapToObj(i -> new Music(genres[i], plays[i], i))
    .collect(Collectors.groupingBy(Music::getGenre))
    .entrySet().stream()
    .sorted((a, b) -> sum(b.getValue()) - sum(a.getValue()))
    .flatMap(x->x.getValue().stream().sorted().limit(2))
    .mapToInt(x->x.id).toArray();
  }

  private int sum(List<Music> value) {
    int answer = 0;
    for (Music music : value) {
      answer+=music.played;
    }
    return answer;
  }
}
```

