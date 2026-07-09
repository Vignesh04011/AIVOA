import Card from "../common/Card";

import BasicInfo from "./BasicInfo";
import DiscussionSection from "./DiscussionSection";
import MaterialsSection from "./MaterialsSection";
import SentimentSection from "./SentimentSection";
import OutcomeSection from "./OutcomeSection";
import FollowupSection from "./FollowupSection";
import Button from "../common/Button";

export default function InteractionForm({
    formData,
    setFormData,
    onSubmit,
    loading,
}) {
  return (
    <Card className="space-y-8">

      <h2 className="text-xl font-semibold text-slate-800">
        Interaction Details
      </h2>

      <BasicInfo
  formData={formData}
  setFormData={setFormData}
/>

      <DiscussionSection
  formData={formData}
  setFormData={setFormData}
/>

<MaterialsSection
  formData={formData}
  setFormData={setFormData}
/>

<SentimentSection
  formData={formData}
  setFormData={setFormData}
/>

<OutcomeSection
  formData={formData}
  setFormData={setFormData}
/>

<FollowupSection
  formData={formData}
  setFormData={setFormData}
/>


<div className="flex justify-end pt-4">
    <Button
    disabled={loading}
    className="
bg-emerald-600
hover:bg-emerald-700
text-white
shadow-lg
hover:shadow-xl
transition-all
duration-200
"
    onClick={onSubmit}
>
        {loading ? "Saving..." : "Log Interaction"}
    </Button>
</div>

    </Card>
  );
}