import RadioGroup from "../common/RadioGroup";

export default function SentimentSection({
  formData,
  setFormData,
}) {
  return (
    <div className="space-y-3">

      <h3 className="text-sm font-semibold text-slate-700">
        Observed HCP Sentiment
      </h3>

      <RadioGroup
  value={formData.sentiment}
  onChange={(value) =>
    setFormData({
      ...formData,
      sentiment: value,
    })
  }
/>

    </div>
  );
}