import { useState } from 'react';
import { RadioData } from '../types';

export default function useRadio(data: RadioData[]) {
  const [radioOptions, setRadioOptions] = useState(data);
  const [chosenValue, setChosenValue] = useState(data[0]);

  const updateRadioValue = (index: number) => {
    setChosenValue(radioOptions[index]);
  };

  const resetChosenValue = () => {
    setChosenValue(data[0]);
  };

  return { radioOptions, chosenValue, updateRadioValue, resetChosenValue };
}
