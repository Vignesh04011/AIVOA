import Input from "../common/Input";
import TextArea from "../common/TextArea";
import Button from "../common/Button";

export default function DiscussionSection() {
  return (
    <div className="space-y-5">

      <Input
        label="Attendees"
        placeholder="Enter names or search..."
      />

      <TextArea
        label="Topics Discussed"
        placeholder="Enter key discussion points..."
        rows={4}
      />

      <Button>
        🎤 Summarize from Voice Note
      </Button>

    </div>
  );
}