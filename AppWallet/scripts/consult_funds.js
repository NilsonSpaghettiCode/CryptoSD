import { consumeService, setRequestOptions } from './consume_service.js'

import { config } from '../config/config.js'

const alerts = document.getElementById('alerts')

const header_label_account = document.getElementById('wallet_header')

header_label_account.textContent = localStorage['wallet_account']

document.getElementById('btn_consult').addEventListener('click', e => {
    consult_wallet()
})

function consult_wallet() {
    console.log('Consultar wallet')
    let wallet = document.getElementById('wallet').value

    let formdata = new FormData()
    formdata.append('wallet', wallet.trim())

    let requestOptions = setRequestOptions('POST', formdata)
    let response = consumeService(config.services[0]['consult_funds_url'], requestOptions, processResponse, processError)


}

function processResponse(response) {
    //console.log(response)

    setAlertSucess(response)

}

function processError(error) {
    setAlertError(error)
}

function setAlertSucess(response) {
    console.log(response)
    if (response['activate']) {
        let exists = response['content']['exists']
        if (exists) {
            alerts.className = "alert alert-success"
            let account = response['content']['request_wallet']
            let amount = response['content']['amount']
            alerts.textContent = `Your wallet is '${account}' with a total of $ ${amount}`
            localStorage['wallet_account'] = account
        } else {
            let account = response['content']['request_wallet']
            alerts.className = "alert alert-warning"
            alerts.textContent = `The wallet ${account} doesn't exist...`
        }
    } else {
        alerts.textContent = 'Some service is down'
        alerts.className = "alert alert-danger"
    }

}

function setAlertError(error) {

    alerts.textContent = 'The service Main Crypto is unavailable ...'
    alerts.className = "alert alert-danger"
}
