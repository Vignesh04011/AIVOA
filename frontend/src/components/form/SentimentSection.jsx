import RadioGroup from "../common/RadioGroup";

export default function SentimentSection() {
  return (
    <div className="space-y-3">

      <h3 className="text-sm font-semibold text-slate-700">
        Observed HCP Sentiment
      </h3>

      <RadioGroup />

    </div>
  );
}