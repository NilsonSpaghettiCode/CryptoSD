import { consumeService,setRequestOptions } from './consume_service.js'
import {config} from '../config/config.js'

const header_label_account = document.getElementById('wallet_header')

header_label_account.textContent = localStorage['wallet_account']