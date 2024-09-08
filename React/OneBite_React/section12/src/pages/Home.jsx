import { useState, useContext } from "react";
import { DiaryStateContext } from "../App";


import Header from "../components/Header";
import Button from "../components/Button";
import DiaryList from "../components/DiaryList";

const getMonthlyData = (pivotDate, data) => {
  // 해당 월의 시작점. 1일 0시 0분 0초
  const beginTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth(),
    1,
    0,
    0,
    0
  ).getTime();
  
  // 마지막 시간 (이전 달의 바로 전)
  const endTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth() + 1,
    0,
    23,
    59,
    59
  ).getTime();
  return data.filter((item) => beginTime <= item.createdDate && item.createdDate <= endTime) ;
};


const Home = () => {
  const data = useContext(DiaryStateContext);
  const [pivotDate, setPivitDate] = useState(new Date());

  const monthlyData = getMonthlyData(pivotDate, data);

  

  const IncreaseMonth = () => {
    setPivitDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() + 1));
  };
  const DecreaseMonth = () => {
    setPivitDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() - 1));
  };

  return (
    <div>
      <Header
        title={`${pivotDate.getFullYear()}년 ${pivotDate.getMonth() + 1}월`}
        leftchild={<Button onClick={DecreaseMonth} text={"<"} />}
        rightchild={<Button onClick={IncreaseMonth} text={">"} />}
      />
      <DiaryList data={monthlyData}/>
    </div>
  );
};

export default Home;
