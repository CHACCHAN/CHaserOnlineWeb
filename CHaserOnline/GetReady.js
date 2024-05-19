function GetReady(returnNumber, ActionReturnNumber) {
    var GetReadyMode = 4;
    var param;

    if(ActionReturnNumber[1] >= 70 && ActionReturnNumber[1] <= 79) {
        GetReadyMode = 1;
    } else if(ActionReturnNumber[3] >= 70 && ActionReturnNumber[3] <= 79) {
        GetReadyMode = 3;
    } else if(ActionReturnNumber[5] >= 70 && ActionReturnNumber[5] <= 79) {
        GetReadyMode = 5;
    } else if(ActionReturnNumber[7] >= 70 && ActionReturnNumber[7] <= 79) {
        GetReadyMode = 7;
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

window.GetReady = GetReady;