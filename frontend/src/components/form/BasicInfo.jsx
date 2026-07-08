import Input from "../common/Input";
import Select from "../common/Select";

export default function BasicInfo() {
  return (
    <div className="grid grid-cols-2 gap-5">

      <Input
        label="HCP Name"
        placeholder="Search or select HCP..."
      />

      <Select
        label="Interaction Type"
        options={[
          "Meeting",
          "Call",
          "Email",
        ]}
      />

      <Input
        label="Date"
        type="date"
      />

      <Input
        label="Time"
        type="time"
      />

    </div>
  );
}