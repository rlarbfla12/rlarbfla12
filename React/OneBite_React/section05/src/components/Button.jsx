// Event Handling : 이벤트가 발생했을 때 그것을 처리하는 것 
// ex) 버튼 클릭시 경고창 노출



const Button = ({text, color, children}) => {
    console.log({text, color});

    // 합성 이벤트 객체 e
    const onClickButton = (e) => {
        console.log(e);
        
        console.log(text);
        
    }
    
    return <button 
            onClick={onClickButton}
            // onMouseEnter={onClickButton}
        style={{color: color}}>
        {text} - {color.toUpperCase ()}
        {children}
        </button>;
};

Button.defaultProps = {
    color :"black",
}

export default Button;