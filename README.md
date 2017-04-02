# eareeg-backend
Backend of EarEEG project
## Cloning
Because of the use of submodules, make sure when cloning you run the following command:

```
git clone --recursive git@github.com:EarEEG/eareeg-backend.git
```

## API
The backend sends data to be visualized on the frontend through websockets. The JSON messages will look as follows, with only the client id being required:

```json
{
    "client_id": client_id (string),
    "data": [{
        "type": data_type (string),
        "value": data_value (int),
    }],
}
```

The data\_type parameter can be any of the following:

* attention
* meditation
* rawValue
* delta
* theta
* lowAlpha
* highAlpha
* lowBeta
* highBeta
* lowGamma
* midGamma
* poorSignal
* blinkStrength

Most of the values are transmitted around once a second, but rawValue is sampled around 128 times a second. Due to this, the program transmits rawValue at incremental intervals instead of all at once. The data will be transmitted over a web socket using the "data" event.
