import TextArea from "../common/TextArea";

export default function OutcomeSection({
  formData,
  setFormData,
}) {
  return (
    <TextArea
  label="Outcomes"
  placeholder="Key outcomes or agreements..."
  rows={3}
  value={formData.outcomes}
  onChange={(e) =>
    setFormData({
      ...formData,
      outcomes: e.target.value,
    })
  }
/>
  );
}