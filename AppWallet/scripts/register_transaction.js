import { consumeService, setRequestOptions } from './consume_service.js'
import { config } from '../config/config.js'

const header_label_account = document.getElementById('wallet_header')
const alerts = document.getElementById('alerts')
header_label_account.textContent = localStorage['wallet_account']

document.getElementById('btn_transaction').addEventListener('click', e => {
    makeTransaction()
})

function makeTransaction() {
    //console.log("Entrando")

    let from_wallet = document.getElementById('from_wallet').value
    let to_wallet = document.getElementById('to_wallet').value
    let amount_transaction = document.getElementById('amount_transaction').value

    let format_amount_transaction = parseInt(amount_transaction)

    if (!Number.isNaN(format_amount_transaction)) {
        let formdata = new FormData()

        //Set field as formdata
        formdata.append('from_wallet', from_wallet.trim())
        formdata.append('to_wallet', to_wallet.trim())
        formdata.append('amount', format_amount_transaction)

        let requestOptions = setRequestOptions('POST', formdata)
        consumeService(config.services[1]['register_transaction_url'], requestOptions, processResponse, processError)

        document.getElementById('control-number').style.display = "None"
    } else {
        const control_numbers = document.getElementById('control-number')
        control_numbers.className = "alert alert-warning"
        control_numbers.textContent = "Please enter a valid number..."

        document.getElementById('amount_transaction').focus()
    }

}

function processResponse(response) {

    setAlertSuccess(response)
}
function processError(error) {
    console.log(error)
    setAlertError()
}

function setAlertSuccess(response) {
    //console.log(response)
    if (response['active']) {
        let content_response_transaction = response['content']['transaction']
        let content_response = response['content']

        let from_wallet_response = content_response_transaction['from_wallet']
        let to_wallet_responese = content_response_transaction['to_wallet']
        let amount = content_response_transaction['amount']

        let transaction_done = content_response['transaction_done']
        let transaction_valid = content_response['transaction_valid']

        if (transaction_valid) {
            if (transaction_done) {
                alerts.className = "alert alert-info"
                alerts.textContent = `The transaction from wallet ${from_wallet_response} to wallet ${to_wallet_responese} with amount ${amount} was done`
            } else {
                alerts.className = "alert alert-warning"
                alerts.textContent = `The transaction from wallet ${from_wallet_response} to wallet ${to_wallet_responese} with amount ${amount} wasn't done`
            }
        } else {
            alerts.className = "alert alert-danger"
            alerts.textContent = `The transaction from wallet ${from_wallet_response} to wallet ${to_wallet_responese} with amount ${amount} was invalid`
        }
    } else {
        alerts.className = "alert alert-danger"
        alerts.textContent = `Some service is down`

    }
}

function setAlertError() {
    alerts.className = "alert alert-danger"
    alerts.textContent = `The service Main Crypto is unavailable ...`
}
