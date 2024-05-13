export default function Action(returnNumber, ActionReturnNumber) {
    var mode = 1;
    var param;

    if(returnNumber[1] === 80) {
        mode = 1;
    } else {
        mode = 4;
    }

    switch(mode) {
        case 1:
            param = 'wu';
            break;
        case 3:
            param = 'wl';
            break;
        case 5:
            param = 'wr';
            break;
        case 7:
            param = 'wd';
            break;
        default:
            param = 'wu';
    }

    return param;
}