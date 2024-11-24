var chessBoard = document.querySelector(".chess_board");

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

var number = 1;
for (var i = 1; i < 9; i++) {
    for (var j = 1; j < 9; j++) {
        if (j % 2 == 0) {
            var square = document.createElement('div');
            if (i % 2 != 0) {
                square.className = `board_square square square${number}`;
            }
            else {
                square.className = `board_square_odd square square${number}`;
            }
            chessBoard.append(square);
        }
        else {
            var square = document.createElement('div');
            if (i % 2 == 0) {
                square.className = `board_square square square${number}`;
            }
            else {
                square.className = `board_square_odd square square${number}`;
            }
            chessBoard.append(square);
        }
        number++;
    }
}
console.log(`.square${getRandomInt(64)}`)
var knightSquare = document.querySelector(`.square${getRandomInt(64)}`);
var knightPiece = document.createElement('div');
knightPiece.innerHTML = '<svg class="knightPiece" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M226.6 48L117.3 48l17.1 12.8c6 4.5 9.6 11.6 9.6 19.2s-3.6 14.7-9.6 19.2l-6.5 4.9c-10 7.5-16 19.3-16 31.9l-.3 91c0 10.2 4.9 19.9 13.2 25.8l1.9 1.3c9.9 7.1 23.3 7 33.2-.1l49.9-36.3c10.7-7.8 25.7-5.4 33.5 5.3s5.4 25.7-5.3 33.5l-49.9 36.3-53.8 39.1c-7.3 5.3-13 12.2-16.9 20.1l-50.7 0c5.3-22.1 17.8-41.9 35.9-56.3c-1.3-.8-2.6-1.7-3.8-2.6L97 291.8c-21-15-33.4-39.2-33.3-65l.3-91c.1-19.8 6.7-38.7 18.6-53.9l-.4-.3C70.7 73 64 59.6 64 45.3C64 20.3 84.3 0 109.3 0L226.6 0C331.2 0 416 84.8 416 189.4c0 11.1-1 22.2-2.9 33.2L390.1 352l-48.8 0 24.5-137.8c1.5-8.2 2.2-16.5 2.2-24.8C368 111.3 304.7 48 226.6 48zM85.2 432L68.7 464l310.7 0-16.6-32L85.2 432zm315.7-30.7l26.5 51.2c3 5.8 4.6 12.2 4.6 18.7c0 22.5-18.2 40.8-40.8 40.8L56.8 512C34.2 512 16 493.8 16 471.2c0-6.5 1.6-12.9 4.6-18.7l26.5-51.2C52.5 390.7 63.5 384 75.5 384l297 0c12 0 22.9 6.7 28.4 17.3zM172 128a20 20 0 1 1 0 40 20 20 0 1 1 0-40z"/></svg>';
knightSquare.append(knightPiece);

searchField.addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode;
    if (key === 13) { // код клавиши Enter
        searchButton.click();
    }
});