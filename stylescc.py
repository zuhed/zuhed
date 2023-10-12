@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,500;1,900&display=swap');
*{
    font-family: 'Poppins',cursive;
}
body{
    color: azure;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: black;
}
.greetings{
    font-size: 6rem;
    font-weight: 900;
}
.greetings > span{
    animation: glow 2.5s ease-in-out infinite;
}
@keyframes glow{
    0%, 100%{
        color: #fff;
        text-shadow: 0 0 12px #39c6d6, 0 0 50px #39c6d6, 0 0 100px #39c6d6;
    }
    10%, 90%{
        color: #111;
        text-shadow: none;
    }
}
.greetings > span:nth-child(2){
    animation-delay: .2s ;
}
.greetings > span:nth-child(3){
    animation-delay: .4s ;
}
.greetings > span:nth-child(4){
    animation-delay: .6s;
}
.greetings > span:nth-child(5){
    animation-delay: .8s;
}
.greetings > span:nth-child(6){
    animation-delay: 1.2s ;
}
.greetings > span:nth-child(7){
    animation-delay: 1.4s ;
}
.greetings > span:nth-child(8){
    animation-delay: 1.6s;
}
.greetings > span:nth-child(9){
    animation-delay: 1.8s;
}

.description{
    font-size: 1.5rem;
    margin-bottom: 20px;
}

.button a{
    text-decoration: none;
    font-size: 1rem;
    color: #111;
}

@media screen and (max-width:574px){
    .greetings{
        display: block;
        font-size: 3rem;
        font-weight: 500;
        text-align: center;
    }
    .description{
        font-size: 1rem;
    }
    
    .button a{
        font-size: .5rem;
    }
}