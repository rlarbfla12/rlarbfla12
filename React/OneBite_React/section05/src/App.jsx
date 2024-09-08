// jsx : 확장된 자바스트립트 문법

import "./App.css";
import Register from "./components/Register";
import HookExam from "./components/HookExam";

// app 컴포넌트 반환
// 다른 컴포넌트들은 app안에 자식컴포넌트로 존재해야 함
// app에서 불러오기 (app = 루트 컴포넌트 main.jsx)

// useState함수안에는 현재값을 받고, 그리고 그걸 사용하는 함수값이 들어있음

function App() {
  return (
    <>
      {/* <Register /> */}
      <HookExam />
    </>
  );
}

export default App;
