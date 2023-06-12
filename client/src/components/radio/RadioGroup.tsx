import { RadioData } from '../../types';
import Radio from './Radio';

const RadioGroup = ({
  data,
  chosenValue,
  update,
}: {
  data: RadioData[];
  chosenValue: string;
  update: (index: number) => void;
}) => {
  return (
    <ul className="flex flex-col items-start my-2">
      {data.map((radioValue: string, index: number) => {
        return (
          <Radio
            key={radioValue}
            label={radioValue}
            chosenValue={chosenValue}
            onChange={() => update(index)}
          />
        );
      })}
    </ul>
  );
};

export default RadioGroup;
