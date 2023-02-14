package jpabook.enumtest;
        
import org.apache.commons.lang3.StringUtils;

import javax.el.MethodNotFoundException;
import java.lang.annotation.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.stream.Stream;

// solve to
// a) define annotation @Command
// b) write function RunCommand.printCommands(), RunCommand.doCommand()
// java reflection

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface Command {
    String value();

}

class SomeObject {
    @Command("say")
    void doSay(String word) {
        System.out.println("say " + word);
    }

    @Command("tell")
    void doTell(String word) {
        System.out.println("tell " + word);
    }

    @Command("think")
    void thinkAbout(String word) {
        System.out.println("think about " + word);
    }
}

public class RunCommand {

    void printCommands(SomeObject o) {
        getDeclaredMethodsFromObject(o).filter(method -> hasTargetAnnotation(method, Command.class))
                .map(RunCommand::getMethodInfo).forEach(System.out::println);
    }

    void doCommand(SomeObject o, String methodName, String value) {
        getDeclaredMethodsFromObject(o)
                .filter(method -> hasTargetAnnotation(method, Command.class))
                .filter(method -> isSameMethodName(method, methodName))
                .findAny().ifPresentOrElse(method -> doInvoke(method, o, value),
                        () -> { throw new MethodNotFoundException("허용하지 않는 메서드입니다");});
    }

    void main(String args[]){
        SomeObject o = new SomeObject();

        printCommands(o);
        // print out below example
        // say => doSay
        // tell => doTell
        // think => thinkAbout

        doCommand(o, "say", "hello");
        // say hello
        doCommand(o, "think", "world");
        // think about world
    }

    private Stream<Method> getDeclaredMethodsFromObject(Object o) {
        return Arrays.stream(o.getClass().getDeclaredMethods());
    }

    private boolean hasTargetAnnotation(Method method, Class<? extends Annotation> target) {
        return method.getAnnotation(target) != null;
    }

    private String getMethodInfo(Method method) {
        return method.getAnnotation(Command.class).value() + " => " + method.getName();
    }

    private boolean isSameMethodName(Method method, String methodName) {
        return StringUtils.equals(method.getAnnotation(Command.class).value(), methodName);
    }

    private void doInvoke(Method method, Object target, String value) {
        try {
            method.invoke(target, value);
        } catch (IllegalAccessException | InvocationTargetException e) {
            System.out.println("에너테이션 메소드 실행 중 에러 발생" + e);
        }
    }

}