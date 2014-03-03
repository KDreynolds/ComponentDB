/*
   Copyright (c) 2004-2005 The University of Chicago, as Operator
   of Argonne National Laboratory.
*/
package CFWDemo;

import net.javaprog.ui.wizard.AbstractStep;
import net.javaprog.ui.wizard.Step;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JComponent;

public class DemoWizardFinishStep extends AbstractStep {

    public DemoWizardFinishStep() {
        super("Finish","You are done.");
        setCanFinish(true);
    }

    protected JComponent createComponent() {
        // return component to be shown to the user
        JPanel stepComponent = new JPanel();
        stepComponent.add(new JLabel("You're done. Click Finish> to close."));
        return stepComponent;
    }

    public void prepareRendering() {
    }

}
