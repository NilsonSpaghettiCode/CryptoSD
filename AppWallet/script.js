import { consumeService,setRequestOptions } from './scripts/consume_service.js'
import {config} from './config/config.js'

const alerts = document.getElementById('alerts')
const header_label_account = document.getElementById('wallet_header')

header_label_account.textContent = localStorage['wallet_account']
function create_wallet() {
    let name_user = document.getElementById('name_user').value

    let formdata = new FormData()
    formdata.append('name_user',name_user)

    let requestOptions = setRequestOptions('POST', formdata)
    let response = consumeService(config.services[2]['create_wallet_url'], requestOptions, processResponse ,processError)

}


function processResponse(response) {
    //console.log(response)

    setAlertSucess(response)
    
    
}
function processError(error)
{
    setAlertError(error)
}

document.getElementById('btn_create').addEventListener('click', e => {
    create_wallet()
})

function setAlertSucess(response)
{
    console.log(response)
    let exists = response['content']['exist']
    if(!exists)
    {
        alerts.className = "alert alert-success"
        let account = response['content']['account']
        let user = response['content']['user']
        alerts.textContent = `Your wallet is ${account} associate to ${user}`
        localStorage['wallet_account'] = account

    }else
    {
        let user = response['content']['user']
        alerts.className = "alert alert-warning"
        alerts.textContent = `The User ${user} already exist...`
    }
    
    
}

function setAlertError(error)
{

    alerts.textContent = 'The services of CryptoSD are unavailable...'
    alerts.className = "alert alert-danger"
}



