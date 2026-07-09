import Card from "../common/Card";

import AssistantHeader from "./AssistantHeader";
import AssistantMessages from "./AssistantMessages";
import AssistantInput from "./AssistantInput";

export default function AssistantPanel({

    messages,

    loading,

    onSend,

}) {

    return (

        <Card className="flex h-[750px] flex-col">

            <AssistantHeader />

            <AssistantMessages

                messages={messages}

                loading={loading}

            />

            <AssistantInput

                loading={loading}

                onSend={onSend}

            />

        </Card>

    );

}