# PageController & TabController 예제



```dart
import 'package:flutter/material.dart';

class PageviewExample extends StatefulWidget {
  PageviewExample({Key? key}) : super(key: key);

  @override
  State<PageviewExample> createState() => _PageviewExampleState();
}

class _PageviewExampleState extends State<PageviewExample>
    with SingleTickerProviderStateMixin {
  int _page = 0;
  late PageController _pController;
  late TabController _tController;

  @override
  void initState() {
    super.initState();
    _pController = PageController();
    _tController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _pController.dispose();
    _tController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('PageView example'),
        bottom: TabBar(
          controller: _tController,
          onTap: (value) {
            _page = value;
            _pController.animateToPage(_page,
                duration: Duration(milliseconds: 300), curve: Curves.ease);
          },
          tabs: [
            Tab(icon: Icon(Icons.looks_one_rounded)),
            Tab(icon: Icon(Icons.looks_two_rounded)),
            Tab(icon: Icon(Icons.looks_3_rounded)),
          ],
        ),
      ),
      body: PageView(
        controller: _pController,
        scrollDirection: Axis.horizontal,
        onPageChanged: (value) {
          _page = value;
          _tController.animateTo(_page,
              duration: Duration(milliseconds: 300), curve: Curves.ease);
        },
        children: [
          _container(1, Colors.red),
          _container(2, Colors.green),
          _container(3, Colors.blue),
        ],
      ),
    );
  }

  Container _container(int page, Color color) {
    return Container(
        height: 100000,
        color: color,
        child: Center(
            child: Text(
          'Page $page',
          style: TextStyle(
              color: Colors.white, fontWeight: FontWeight.bold, fontSize: 24),
        )));
  }
}

```
