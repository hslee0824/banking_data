import PrimaryContainer from './components/common/PrimaryContainer';
import useRadio from './hooks/useRadio';
import CheckboxGroup from './components/checkbox/CheckboxGroup';
import useCheckbox from './hooks/useCheckbox';
import RadioGroup from './components/radio/RadioGroup';
import { useState } from 'react';
import { Slider } from './components/slider/Slider';
import SliderWrapper from './components/slider/SliderWrapper';
import SubmitButton from './components/common/SubmitButton';
import ResetButton from './components/common/ResetButton';
import { processedModel } from './controller';

const allToppings = [
  { name: 'Golden Corn', checked: false },
  { name: 'Paneer', checked: false },
  { name: 'Tomato', checked: false },
  { name: 'Mushroom', checked: false },
  { name: 'Onion', checked: false },
  { name: 'Black Olives', checked: false },
];

const radio = ['option1', 'option2'];

function App() {
  const { checkboxArray, updateCheckStatus, resetCheckStatus } =
    useCheckbox(allToppings);
  const { radioOptions, chosenValue, updateRadioValue, resetChosenValue } =
    useRadio(radio);
  // make this range depend on some logic
  const sliderDefaultValue = [33];
  const [sliderValue, setSliderValue] = useState(sliderDefaultValue);
  const sliderValueRange = [0, 100];

  const finalValue = {
    column_1: checkboxArray
      .filter((item) => item.checked)
      .map((item) => item.name),
    column_2: chosenValue,
    column_3: sliderValue[0],
  };

  function handleReset() {
    resetCheckStatus();
    resetChosenValue();
    setSliderValue(sliderDefaultValue);
  }

  return (
    <main className="py-12 w-full h-fit flex flex-col items-center gap-10 ">
      <img
        className="-z-10 fixed inset-0 w-screen h-screen object-cover md:object-top"
        // src="https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png"
        src="/images/preview.jpg"
      />
      <PrimaryContainer>
        <h1 className="font-bold text-3xl md:text-4xl">
          House Price Prediction App
        </h1>
      </PrimaryContainer>
      <PrimaryContainer>
        <h2 className="font-bold text-2xl text-left">
          Please select xxx of the house you want to predict the price of:
        </h2>
        <CheckboxGroup data={checkboxArray} update={updateCheckStatus} />
        <p className="w-full h-fit">{JSON.stringify(checkboxArray)}</p>
      </PrimaryContainer>
      <PrimaryContainer>
        <RadioGroup
          data={radioOptions}
          chosenValue={chosenValue}
          update={updateRadioValue}
        />
        <p>
          <pre>{chosenValue}</pre>
        </p>
      </PrimaryContainer>
      <PrimaryContainer>
        <SliderWrapper
          name="Something"
          value={sliderValue}
          min={sliderValueRange[0]}
          max={sliderValueRange[1]}
        >
          <Slider
            defaultValue={sliderDefaultValue}
            min={sliderValueRange[0]}
            max={sliderValueRange[1]}
            step={1}
            onValueChange={(e) => setSliderValue(e)}
            value={sliderValue}
          />
        </SliderWrapper>
      </PrimaryContainer>
      <PrimaryContainer className="flex gap-4 justify-center">
        <ResetButton
          onClick={() => {
            handleReset();
          }}
        >
          Reset
        </ResetButton>
        <SubmitButton
          onClick={() => {
            // processedModel.postData(finalValue);
            console.log(finalValue);
          }}
        >
          Submit
        </SubmitButton>
      </PrimaryContainer>
    </main>
  );
}

export default App;
