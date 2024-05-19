async function loadScript(url) {
    return new Promise((resolve, reject) => {
        const existingScript = document.querySelector(`script[src="${url}"]`);
        if (existingScript) {
            console.log(`Removing existing script: ${url}`);
            existingScript.remove();
        }

        const script = document.createElement('script');
        script.src = url;
        script.type = 'text/javascript';
        script.onload = () => {
            console.log(`Loaded script: ${url}`);
            resolve(script);
        };
        script.onerror = (e) => {
            console.error(`Failed to load script: ${url}`, e);
            reject(new Error(`Failed to load script: ${url}`));
        };
        document.head.appendChild(script);
        console.log(`Appending script: ${url}`);
    });
}

async function importDependencies() {
    await loadScript('http://localhost:8080/api/chaseronline/js/GetReady.js');
    await loadScript('http://localhost:8080/api/chaseronline/js/Action.js');

    const GetReady = window.GetReady;
    const Action = window.Action;
    return { GetReady, Action };
}

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
        const { GetReady } = await importDependencies();
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
        const { Action } = await importDependencies();
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