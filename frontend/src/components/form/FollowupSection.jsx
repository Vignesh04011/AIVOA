import TextArea from "../common/TextArea";

export default function FollowupSection() {
  return (
    <TextArea
      label="Follow-up Actions"
      placeholder="Enter next steps..."
      rows={3}
    />
  );
}