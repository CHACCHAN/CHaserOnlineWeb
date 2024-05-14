import GetReady from '../../../../CHaserOnline/GetReady.js';
import Action from '../../../../CHaserOnline/Action.js';

export default class CHaserOnlineController {
    constructor(options) {
        this._url = options?.url;
        this._proxy = options?.proxy;
        this._debug = options?.debug;
        this._user = options?.user;
        this._password = options?.password;
        this._room = options?.room;
        this._returnNumber = new Array();
        this._ActionReturnNumber = new Array();
        this._gameSet = true;
    }

    async connect() {
        const response = await fetch('http://localhost:8080/api/chaseronline/connect', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                url: this._url,
                proxy: this._proxy,
                debug: this._debug,
                user: this._user,
                password: this._password,
                room: this._room,
            })
        }).then((response) => response.json());

        return response;
    }

    async getready() {
        await fetch('http://localhost:8080/api/chaseronline/getready', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'GetReadyMode': GetReady(this._returnNumber, this._ActionReturnNumber) })
        })
        .then((response) => response.json())
        .then((res) => this._returnNumber = res);
        console.log(this._returnNumber);

        return this._returnNumber;
    }

    async action() {
        await fetch('http://localhost:8080/api/chaseronline/action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'mode': Action(this._returnNumber, this._ActionReturnNumber) })
        })
        .then((response) => response.json())
        .then((res) => this._ActionReturnNumber = res);
        console.log(this._ActionReturnNumber);

        return this._ActionReturnNumber;
    }

    async gameSet() {
        await fetch('http://localhost:8080/api/chaseronline/gameset')
        .then((response) => response.json())
        .then((res) => this._gameSet = res);
        console.log(this._gameSet)
        return this._gameSet;
    }
}