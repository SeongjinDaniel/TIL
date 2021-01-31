# Axios



```react
<button className="btn btn-primary" onClick={() => {
        axios.get('https://codingapple1.github.io/shop/data2.json')
            .then((result) => {
            console.log(result.data)
        })
            .catch(() => {
            console.log('실패했어요')
        })
    }}>더보기</button>
```

