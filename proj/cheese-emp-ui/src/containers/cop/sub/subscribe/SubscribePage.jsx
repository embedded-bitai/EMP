import React from "react";

import * as Survey from "survey-react";
import "survey-react/modern.css";

import { json } from './Subscribe_json'

Survey.StylesManager.applyTheme("modern");

Survey
    .Serializer
    .addProperty("page", {
        name: "navigationTitle:string",
        isLocalizable: true
    });
Survey
    .Serializer
    .addProperty("page", {
        name: "navigationDescription:string",
        isLocalizable: true
    });
    
function onValueChanged(result) {
    console.log("value changed!" + JSON.stringify(result))
}

function onComplete(result) {
    console.log("Complete!" + JSON.stringify(result.data))

}

export default function SubscribePage () {
    var model = new Survey.Model(json)
    return (
        <div className="container">
            <Survey.Survey
                model={model}
                onComplete={onComplete}
                onValueChanged={onValueChanged}
            />
        </div>
    )
}