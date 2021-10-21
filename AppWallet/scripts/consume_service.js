

export function setRequestOptions(method_request, formdata, redirect='follow')
{
  let requestOptions = {
      method: method_request,
      body: formdata,
      redirect: redirect
    }
      return requestOptions
}

export function consumeService(url, requestOptions,processFunctionResponse ,processFunctionError) {
    fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => processFunctionResponse(result))
  .catch(error => processFunctionError(error));
    
}

