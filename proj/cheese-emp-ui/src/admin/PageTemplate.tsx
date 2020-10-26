import React from "react";
import { MainMenu } from "./index"

const PageTemplate = ({children} : { children: any }) => <div className={"page"}>
    <MainMenu/>
    {children}
</div>

export default PageTemplate