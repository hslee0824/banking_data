import { useState } from 'react';
import { CheckboxData } from '../types';

export default function useCheckbox(data: CheckboxData[]) {
  const [checkboxArray, setCheckboxArrayData] = useState(data);

  const updateCheckStatus = (index: number) => {
    setCheckboxArrayData(
      checkboxArray.map((checkbox, currentIndex) =>
        currentIndex === index
          ? { ...checkbox, checked: !checkbox.checked }
          : checkbox
      )
    );
  };

  const resetCheckStatus = () => {
    setCheckboxArrayData(
      checkboxArray.map((checkbox) => ({ ...checkbox, checked: false }))
    );
  };

  return { checkboxArray, updateCheckStatus, resetCheckStatus };
}
