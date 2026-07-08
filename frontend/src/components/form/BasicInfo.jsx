import Input from "../common/Input";
import Select from "../common/Select";
import interactionTypes from "../../constants/interactionTypes";

export default function BasicInfo() {
  return (
    <div className="space-y-5">

      {/* Row 1 */}
      <div className="grid grid-cols-2 gap-5">

        <Input
          label="HCP Name"
          placeholder="Search or select HCP..."
        />

        <Select
          label="Interaction Type"
          options={interactionTypes}
        />

      </div>

      {/* Row 2 */}
      <div className="grid grid-cols-2 gap-5">

        <Input
          label="Date"
          type="date"
        />

        <Input
          label="Time"
          type="time"
        />

      </div>

    </div>
  );
}