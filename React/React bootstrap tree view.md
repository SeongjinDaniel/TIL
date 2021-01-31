# React bootstrap tree view



#### 소스 코드

```jsx
import React, { Component } from "react";
import { Link } from "react-router-dom";
import DivisionAdd from "./divisionAdd";
import Tree from "@naisutech/react-tree";

class DivisionList extends Component {
  render() {
    const myTheme = {
      "my-theme": {
        text: "black",
        bg: "white",
        highlight: "#ebedf3", // the colours used for selected and hover items
        decal: "#3783e7", // the colours used  for open folder indicators and icons
        accent: "#999", // the colour used for row borders and empty file indicators
      },
    };
    const nodes = [
      {
        label: "SDT inc.",
        id: 0,
        parentId: null,
        items: null,
        // items: [
        //   {
        //     label: "File",
        //     parentId: 0,
        //     id: 5678,
        //   },
        // ],
      },
      {
        label: "운영",
        id: 10,
        parentId: null,
        items: null,
      },
      {
        label: "마케팅",
        id: 11,
        parentId: 10,
        items: null,
      },
      {
        label: "BD/세일즈",
        id: 12,
        parentId: 10,
        items: null,
      },
      {
        label: "SCM",
        id: 13,
        parentId: 10,
        items: null,
      },
      {
        label: "생산/품질관리",
        id: 14,
        parentId: 10,
        items: null,
      },
      {
        label: "회계",
        id: 15,
        parentId: 10,
        items: null,
      },
      {
        label: "디바이스",
        id: 20,
        parentId: null,
        items: null,
      },
      {
        label: "기계엔지니어링",
        id: 21,
        parentId: 20,
        items: null,
      },
      {
        label: "하드웨어",
        id: 22,
        parentId: 20,
        items: null,
      },
      {
        label: "시스템코어",
        id: 23,
        parentId: 20,
        items: null,
      },
      {
        label: "펌웨어",
        id: 24,
        parentId: 20,
        items: null,
      },
      {
        label: "서비스",
        id: 30,
        parentId: null,
        items: null,
      },
      {
        label: "플랫폼 개발",
        id: 31,
        parentId: 30,
        items: null,
      },
    ];
    return (
      <article className="wrapper-division-creation">
        <div className="tree-box">
          <div className="subtitle">
            <h2>부서 목록</h2>
          </div>
          <div className="btn-divisionAdd">
            <Link to="/divisions">
              <button className="divisionAdd">부서 추가</button>
            </Link>
          </div>
          <div
            style={{ width: "100%", display: "flex", flexDirection: "column" }}
          >
            <Tree nodes={nodes} theme={"my-theme"} customTheme={myTheme} />
          </div>
          {/*<div style={{ width: '50%', display: 'flex', flexGrow: 1 }}>*/}
          {/*  <Tree nodes={nodes} grow />*/}
          {/*</div>*/}
        </div>
      </article>
      // <>
      //   <article className="wrapper-division-creation">
      //               <div className="innerBox">
      //                   <div className="subtitle">
      //                       <h2>부서 목록</h2>
      //                   </div>

      //                   <div className="btn-divisionAdd">
      //                       <Link to="/divisions">
      //                           <button className="divisionAdd">부서 추가</button>
      //                       </Link>
      //                   </div>
      //                   <div className="row tableBox">
      //                       <table className="divisionListTable">
      //                           <thead>
      //                               <tr className="row">
      //                                   <th className="col-3">부서 번호</th>
      //                                   <th className="col-6">부서명</th>
      //                                   <th className="col-3">상위부서 번호</th>
      //                               </tr>
      //                           </thead>
      //                           <tbody>
      //                               <tr className="row">
      //                                   <td className="col-3">1</td>
      //                                   <td className="col-6">운영실</td>
      //                                   <td className="col-3">1</td>
      //                               </tr>
      //                               <tr className="row">
      //                                   <td className="col-3">2</td>
      //                                   <td className="col-6">디바이스실</td>
      //                                   <td className="col-3">2</td>
      //                               </tr>
      //                               <tr className="row">
      //                                   <td className="col-3">3</td>
      //                                   <td className="col-6">서비스실</td>
      //                                   <td className="col-3">3</td>
      //                               </tr>
      //                               <tr className="row">
      //                                   <td className="col-3">4</td>
      //                                   <td className="col-6">생산실</td>
      //                                   <td className="col-3">4</td>
      //                               </tr>
      //                               <tr className="row">
      //                                   <td className="col-3">5</td>
      //                                   <td className="col-6">가나다</td>
      //                                   <td className="col-3">5</td>
      //                               </tr>
      //                           </tbody>
      //                       </table>
      //                   </div>
      //               </div>
      //           </article>
      // </>
    );
  }
}

export default DivisionList;

```



#### 검색 키워드

- react bootstrap tree view



- **참조**

  - https://reactjsexample.com/a-hierarchical-object-tree-component-for-react/

  - https://codesandbox.io/s/naisu-techreact-tree-demo-oewiz?file=/src/index.js:0-99
  - https://www.npmjs.com/package/@naisutech/react-tree
