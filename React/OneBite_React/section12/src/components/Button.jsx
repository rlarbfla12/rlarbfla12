import "./Button.css";

// text : 버튼글씨, type: 버튼 색(수정, 삭제 등)
const Button = ({ text, type, onClick }) => {
  return (
    <button onClick={onClick} className={`Button Button_${type}`}>
      {text}
    </button>
  );
};

export default Button;
