import TextArea from "../common/TextArea";

export default function FollowupSection({
  formData,
  setFormData,
}) {
  return (
    <TextArea
  label="Follow-up Actions"
  placeholder="Enter next steps..."
  rows={3}
  value={formData.follow_up_actions}
  onChange={(e) =>
    setFormData({
      ...formData,
      follow_up_actions: e.target.value,
    })
  }
/>
  );
}