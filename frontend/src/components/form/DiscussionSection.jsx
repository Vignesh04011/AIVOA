import Input from "../common/Input";
import TextArea from "../common/TextArea";
import Button from "../common/Button";

export default function DiscussionSection({
  formData,
  setFormData,
}) {
  return (
    <div className="space-y-5">

      <Input
  label="Attendees"
  placeholder="Enter names or search..."
  value={formData.attendees}
  onChange={(e) =>
    setFormData({
      ...formData,
      attendees: e.target.value,
    })
  }
/>

<TextArea
  label="Topics Discussed"
  placeholder="Enter key discussion points..."
  rows={4}
  value={formData.topics_discussed}
  onChange={(e) =>
    setFormData({
      ...formData,
      topics_discussed: e.target.value,
    })
  }
/>

      <Button>
        🎤 Summarize from Voice Note
      </Button>

    </div>
  );
}