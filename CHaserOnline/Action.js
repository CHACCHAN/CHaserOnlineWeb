export default function Action(returnNumber, ActionReturnNumber) {
    var mode = 1;
    var param;

    if(returnNumber[1] >= 70 && returnNumber[1] <= 79) {
        mode = 1;
    } else if(returnNumber[3] >= 70 && returnNumber[3] <= 79) {
        mode = 3;
    } else if(returnNumber[5] >= 70 && returnNumber[5] <= 79) {
        mode = 5;
    } else if(returnNumber[7] >= 70 && returnNumber[7] <= 79) {
        mode = 7;
    } else {
        mode = 1;
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