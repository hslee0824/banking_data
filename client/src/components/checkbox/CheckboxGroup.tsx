import { CheckboxData } from '../../types';
import Checkbox from './Checkbox';

const CheckboxGroup = ({
  data,
  update,
}: {
  data: CheckboxData[];
  update: (index: number) => void;
}) => {
  return (
    <ul className="flex flex-col items-start my-2">
      {data.map((checkbox: CheckboxData, index: number) => (
        <Checkbox
          key={checkbox.name}
          checked={checkbox.checked}
          onChange={() => update(index)}
          label={checkbox.name}
        />
      ))}
    </ul>
  );
};

export default CheckboxGroup;
