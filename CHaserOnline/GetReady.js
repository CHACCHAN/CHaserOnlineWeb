export default function GetReady(returnNumber, ActionReturnNumber) {
    var GetReadyMode = 4;
    var param;

    if(ActionReturnNumber[1] === 80) {
        GetReadyMode = 1;
    } else {
        GetReadyMode = 4;
    }

    switch(GetReadyMode) {
        case 1:
            param = 'gru';
            break;
        case 3:
            param = 'grl';
            break;
        case 5:
            param = 'grr';
            break;
        case 7:
            param = 'grd';
            break;
        default:
            param = 'gr';
    }

    return param;
}