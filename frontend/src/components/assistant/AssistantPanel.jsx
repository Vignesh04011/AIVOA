import Card from "../common/Card";

import AssistantHeader from "./AssistantHeader";
import AssistantMessages from "./AssistantMessages";
import AssistantInput from "./AssistantInput";

export default function AssistantPanel() {
  return (
    <Card className="flex h-190 flex-col">

      <AssistantHeader />

      <AssistantMessages />

      <AssistantInput />

    </Card>
  );
}