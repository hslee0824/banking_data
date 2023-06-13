import React from 'react';
import CheckboxGroup from '../components/checkbox/CheckboxGroup';
import RadioGroup from '../components/radio/RadioGroup';
import useRadio from '../hooks/useRadio';
import useCheckbox from '../hooks/useCheckbox';

const allToppings = [
  { name: 'Golden Corn', checked: false },
  { name: 'Paneer', checked: false },
  { name: 'Tomato', checked: false },
  { name: 'Mushroom', checked: false },
  { name: 'Onion', checked: false },
  { name: 'Black Olives', checked: false },
];

const radio = ['option1', 'option2'];

const Page1 = () => {
  const { radioOptions, chosenValue, updateRadioValue, resetChosenValue } =
    useRadio(radio);
  const { checkboxArray, updateCheckStatus, resetCheckStatus } =
    useCheckbox(allToppings);

  const finalValue = {
    column_1: checkboxArray
      .filter((item) => item.checked)
      .map((item) => item.name),
    column_2: chosenValue,
    // column_3: sliderValue[0],
  };

  return (
    <div>
      <CheckboxGroup data={checkboxArray} update={updateCheckStatus} />
      <p className="w-full h-fit">{JSON.stringify(checkboxArray)}</p>
      <RadioGroup
        data={radioOptions}
        chosenValue={chosenValue}
        update={updateRadioValue}
      />
      <p>
        <pre>{chosenValue}</pre>
      </p>
    </div>
  );
};

export default Page1;
