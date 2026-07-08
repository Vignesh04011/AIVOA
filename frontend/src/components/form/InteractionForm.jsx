import Card from "../common/Card";

import BasicInfo from "./BasicInfo";
import DiscussionSection from "./DiscussionSection";
import MaterialsSection from "./MaterialsSection";
import SentimentSection from "./SentimentSection";
import OutcomeSection from "./OutcomeSection";
import FollowupSection from "./FollowupSection";

export default function InteractionForm() {
  return (
    <Card className="space-y-8">

      <h2 className="text-xl font-semibold text-slate-800">
        Interaction Details
      </h2>

      <BasicInfo />

      <DiscussionSection />

      <MaterialsSection />

      <SentimentSection />

      <OutcomeSection />

      <FollowupSection />

    </Card>
  );
}