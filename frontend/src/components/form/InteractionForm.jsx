import Card from "../common/Card";
import BasicInfo from "./BasicInfo";
import DiscussionSection from "./DiscussionSection";

export default function InteractionForm() {
  return (
    <Card>
      <div className="p-6">
        <h2 className="mb-6 text-xl font-semibold">
          Interaction Details
        </h2>

        <BasicInfo />

        <DiscussionSection />
      </div>
    </Card>
  );
}